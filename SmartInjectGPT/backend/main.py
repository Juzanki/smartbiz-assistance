from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from pathlib import Path

# === Logging Setup ===
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "server.log"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(str(LOG_FILE), encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# === Kernel Load ===
from backend.kernel.smartinject_kernel import kernel

# === Router Imports ===
from backend.routes import dream_logs
from backend.auth import auth_routes  # NEW
from backend.routes import user_routes  # OPTIONAL if exists

# === App Initialization ===
app = FastAPI(
    title="SmartInjectGPT API",
    version="1.0.0",
    description="Secure Backend for SmartInjectGPT system",
    docs_url="/docs",
    redoc_url="/redoc"
)

# === CORS Configuration ===
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://your-production-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === System Boot Trigger ===
@app.on_event("startup")
def on_startup():
    logging.info("\ud83d\udd27 Booting SmartInjectGPT Kernel...")
    try:
        kernel.observe("\ud83d\ude80 Startup Triggered")
        kernel.decide_and_act()
        logging.info("\u2705 Kernel initialized successfully.")
    except Exception as e:
        logging.exception(f"\u274c Kernel startup failed: {e}")

# === Root Health Check ===
@app.get("/", tags=["System"])
def read_root():
    return {
        "message": "\u2705 SmartInjectGPT Backend is running!",
        "kernel_identity": kernel.identity
    }

# === Route Registration ===
app.include_router(dream_logs.router, prefix="/dreams", tags=["Dream Logs"])
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
# app.include_router(user_routes.router, prefix="/users", tags=["Users"])  # Optional if implemented
