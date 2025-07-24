"""
📦 Database Configuration for SmartBiz Assistance (PostgreSQL)
🔐 Loads environment variables securely from `.env.local` or `.env.production`, 
    initializes SQLAlchemy engine, session, and Base.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ======================== 📁 BASE DIRECTORY ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================== ⚙️ ACTIVE ENVIRONMENT SWITCH ========================
ACTIVE_DB = os.getenv("ACTIVE_DB", "local").strip().lower()

# Load the correct .env file
ENV_FILE = BASE_DIR / "backend" / (".env.production" if ACTIVE_DB == "railway" else ".env.local")

if not ENV_FILE.exists():
    raise FileNotFoundError(f"⚠️ Could not find env file at {ENV_FILE}")

load_dotenv(dotenv_path=ENV_FILE, override=True)

print(f"🔍 Loaded environment: ACTIVE_DB={ACTIVE_DB}")

# ======================== 🔗 GET DATABASE URL ========================
if ACTIVE_DB == "railway":
    DATABASE_URL = os.getenv("RAILWAY_DATABASE_URL")
else:
    DATABASE_URL = os.getenv("LOCAL_DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        f"❌ DATABASE_URL is missing.\n👉 Expected key: "
        f"{'RAILWAY_DATABASE_URL' if ACTIVE_DB == 'railway' else 'LOCAL_DATABASE_URL'}"
    )

# ======================== 🔗 DATABASE ENGINE & SESSION ========================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ======================== 🧱 DECLARATIVE BASE ========================
Base = declarative_base()

# ======================== 🔁 FASTAPI DB DEPENDENCY ========================
def get_db():
    """
    Provides a SQLAlchemy session to FastAPI endpoints.
    Ensures the session is closed after the request is completed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
