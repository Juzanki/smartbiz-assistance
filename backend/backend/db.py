"""
📦 Database configuration and session management for SmartBiz Assistance (PostgreSQL).
🔒 Loads .env variables securely and sets up SQLAlchemy engine + session.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ========== 📁 BASE DIRECTORY AND .ENV ==========
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

# ========== 🌐 DATABASE URL ==========
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("❌ DATABASE_URL not found in .env file. Please check configuration.")

# ========== ⚙️ SQLALCHEMY ENGINE & SESSION ==========
engine = create_engine(DATABASE_URL, pool_pre_ping=True)  # More stable on long connections
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ========== 🧱 DECLARATIVE BASE ==========
Base = declarative_base()

# ========== 🔁 FASTAPI DATABASE DEPENDENCY ==========
def get_db():
    """
    Dependency that provides a DB session to FastAPI endpoints.
    Automatically handles closing after each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
