# === 📦 Imports ===
import os
import logging
from pathlib import Path
from typing import List

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from pydantic import BaseModel

# === 🌍 Load .env Variables ===
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# === 🛠️ Local Modules ===
from backend.db import Base, SessionLocal, engine
from backend.middleware.language import language_middleware
from backend.background import start_background_tasks
from backend.tasks.scheduler import start_schedulers
from backend.websocket import ws_routes, live_ws
from backend.crud.user_crud import get_user_by_identifier, get_user, get_users, create_user
from backend.schemas.user import UserCreate, UserOut as UserResponse

# === 🔁 Core Routes ===
from backend.routes import (
    register, logout, profile, forgot_password, pay_mpesa, pay_pesapal,
    admin_routes, subscription, telegram_bot, broadcast, negotiation_bot,
    voice_assistant, qr_generator, nfc_handler, qr_orders, qr_code,
    nfc_orders, smart_orders, platforms, language, messages, inbox,
    reply, schedule, settings_routes, orders_routes, live_stream,
    campaigns_routes, likes, chat, superchat, announcement,
    guests, fans, filters, viewers, smart_reply, products_live,
    moderation, explore, share_activity,
    host_routes, co_host_routes, co_host_invite_routes,
    gift_fly, replay_gift_timeline, gift_marker, replay_analytics,
    replay_caption, replay_title, replay_summary, live_viewer,
    replay_event_routes, replay_analytics_routes, gift_movement_routes,
    top_contributor_routes, leaderboard_routes, leaderboard_notification_routes
)
from backend.routes.invoice import router as invoice_router
from backend.routes.owner_routes import owner_router
from backend.routes.order_notification import router as order_notification_router
from backend.routes.injection_log_routes import router as injection_log_router
from backend.routes.ai_responder import router as ai_router
from backend.routes.auth_routes import router as auth_router

# === 🚀 Initialize App ===
app = FastAPI(
    title="SmartBiz Assistant API",
    description="Powerful SaaS backend for automating business operations",
    version="1.0.0"
)

# === 🌐 CORS Middleware ===
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    os.getenv("VITE_API_URL", ""),
    os.getenv("VITE_NGROK_URL", ""),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin for origin in origins if origin],
    allow_origin_regex=r"https://.*\.ngrok-free\.app|https://.*\.trycloudflare\.com",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === 🗂️ Static Files & Middleware ===
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.add_middleware(language_middleware)

# === 🧠 DB Init ===
Base.metadata.create_all(bind=engine)

# === 🔁 DB Session Dependency ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === ✅ Env Validation ===
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL is missing in .env")

# === 📝 Logging Setup ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === ⏰ Startup Jobs ===
start_background_tasks()
start_schedulers()

# === 📡 Routers ===
app.include_router(auth_router, prefix="/auth", tags=["Auth"])  # required for login

core_routes = [
    (register.router, "/register-user", ["Register"]),
    (logout.router, "/logout", ["Logout"]),
    (profile.router, None, ["Profile"]),
    (ws_routes.router, None, ["WebSocket"]),
]

for router, prefix, tags in core_routes:
    app.include_router(router, prefix=prefix or "", tags=tags)

# === 🏠 Root Endpoint ===
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "✅ Welcome to SmartBiz Assistant API",
        "docs": "/docs",
        "status": "running"
    }

# === 👤 User Management Endpoints ===
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/", response_model=List[UserResponse], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# === 💬 WhatsApp Test Message ===
class WhatsAppMessage(BaseModel):
    message: str

@app.post("/send-whatsapp/", tags=["WhatsApp"])
async def send_whatsapp_message(message: WhatsAppMessage):
    return {
        "status": "queued",
        "to": os.getenv("RECIPIENT_PHONE", "N/A"),
        "message": message.message
    }

# === 🚀 On Startup ===
@app.on_event("startup")
async def startup_event():
    logging.info("🚀 SmartBiz Assistant backend is starting up...")
    logging.info(f"🔌 Connected to DB: {DATABASE_URL}")

# === ▶️ Entry Point (Local Run) ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
