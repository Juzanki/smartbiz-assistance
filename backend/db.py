"""
Database configuration and session management for SmartBiz SaaS backend.
Loads environment variables and sets up SQLAlchemy with PostgreSQL.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ========== LOAD .env FROM PROJECT ROOT ==========
# Automatically locate .env from the project root (SmartBiz_Assistance/.env)
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# ========== DATABASE URL ==========
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("⚠️ 'DATABASE_URL' environment variable is missing. Check your .env file in project root.")

# ========== SQLALCHEMY SETUP ==========
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ========== DEPENDENCY FUNCTION ==========
def get_db():
    """FastAPI dependency to provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
