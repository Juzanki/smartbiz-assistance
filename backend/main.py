import os
import asyncio
import logging
from typing import List
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from apscheduler.schedulers.background import BackgroundScheduler

# === Load Environment Variables ===
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# === Local Imports ===
from backend.routes import (
    register, auth_routes, logout, profile, forgot_password, pay_mpesa,
    admin_routes, subscription, telegram_bot, broadcast, negotiation_bot,
    voice_assistant, qr_generator, nfc_handler, qr_orders, qr_code,
    nfc_orders, smart_orders, platforms, language, messages, inbox,
    reply, schedule, settings_routes, orders_routes, live_stream
)
from backend.routes.invoice import router as invoice_router
from backend.routes.owner_routes import owner_router
from backend.routes.order_notification import router as order_notification_router
from backend.routes.injection_log_routes import router as injection_log_router
from backend.routes.ai_responder import router as ai_router

from backend.middleware.language import language_middleware
from backend.auth_routes import router as auth_router
from backend.api.smartinject_api import router as smartinject_router
from backend.tasks.scheduler import run_scheduled_task
from backend.crud.user_crud import get_user_by_identifier, get_user, get_users, create_user
from backend.schemas import UserCreate, User as UserResponse
from backend.db import Base, SessionLocal, engine

# === FastAPI Initialization ===
app = FastAPI(
    title="SmartBiz Assistant API",
    description="Powerful SaaS backend for automating business operations",
    version="1.0.0"
)

# === Logging Setup ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === CORS Configuration ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Database Setup ===
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === Environment Check ===
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("❌ 'DATABASE_URL' is missing. Check your .env file inside backend/")

# === Scheduler Setup ===
scheduler = BackgroundScheduler()

def send_scheduled_posts():
    logging.info("✅ Scheduled posts sent")

scheduler.add_job(send_scheduled_posts, "interval", minutes=1)
scheduler.start()

# === Register All Routes ===
routers = [
    (auth_router, None, ["Auth"]),
    (register.router, "/register-user", ["Register"]),
    (auth_routes.router, "/auth", ["Auth-Routes"]),
    (logout.router, "/logout", ["Logout"]),
    (profile.router, None, ["Profile"]),
    (forgot_password.router, "/forgot-password", ["Forgot-Password"]),
    (pay_mpesa.router, None, ["Payments"]),
    (admin_routes.router, None, ["Admin"]),
    (ai_router, "/ai", ["AI Responder"]),
    (subscription.router, "/subscriptions", ["Subscriptions"]),
    (telegram_bot.router, "/telegram", ["Telegram"]),
    (broadcast.router, "/admin", ["Broadcast"]),
    (negotiation_bot.router, None, ["AI Negotiation"]),
    (voice_assistant.router, "/assistant", ["Voice Assistant"]),
    (owner_router, "/owner", ["Owner Panel"]),
    (qr_generator.router, "/qr", ["QR"]),
    (nfc_handler.router, "/nfc", ["NFC"]),
    (qr_orders.router, "/orders", ["Smart Orders"]),
    (qr_code.router, "/qr", ["QR Codes"]),
    (nfc_orders.router, "/nfc", ["NFC Orders"]),
    (smart_orders.router, "/smart-orders", ["Smart Orders"]),
    (order_notification_router, None, ["Order Notification"]),
    (platforms.router, None, ["Platforms"]),
    (language.router, "/user", ["Language"]),
    (messages.router, None, ["Messages"]),
    (inbox.router, None, ["Inbox"]),
    (reply.router, None, ["Reply"]),
    (schedule.router, None, ["Schedule"]),
    (settings_routes.router, None, ["Settings"]),
    (orders_routes.router, None, ["Orders"]),
    (live_stream.router, None, ["Live Stream"]),
    (invoice_router, None, ["Invoice"]),
    (smartinject_router, "/smartinject", ["SmartInject"]),
    (injection_log_router, None, ["Injection Logs"]),
]

for router, prefix, tags in routers:
    app.include_router(router, prefix=prefix or "", tags=tags)

# === Middlewares ===
app.add_middleware(language_middleware)

# === Startup Hook ===
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_scheduled_task())

# === Root Endpoint ===
@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "✅ Welcome to SmartBiz Assistant API",
        "docs": "/docs",
        "status": "running"
    }

# === User CRUD Endpoints ===
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

# === WhatsApp Placeholder ===
class WhatsAppMessage(BaseModel):
    message: str

@app.post("/send-whatsapp/", tags=["WhatsApp"])
async def send_whatsapp_message(message: WhatsAppMessage):
    return {
        "status": "queued",
        "to": os.getenv("RECIPIENT_PHONE", "N/A"),
        "message": message.message
    }

# === Run Server (Only for Local Dev) ===
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
