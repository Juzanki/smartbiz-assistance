"""
📦 SmartBiz Assistance: PostgreSQL Database Configuration
-------------------------------------------------------------
✅ Loads environment variables from `backend/.env.local` or `backend/.env.production`
🛠️ Initializes SQLAlchemy engine, session, and declarative base for ORM
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ========================== 📂 BASE DIRECTORY =============================
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = BASE_DIR / "backend"  # Env files are inside /backend

# ========================== 🌍 ENVIRONMENT DETECTION ======================
# Decide between 'railway' (production) or 'local' (development)
env_choice = os.environ.get("ACTIVE_DB", "local").strip().lower()
env_file = ENV_DIR / (".env.production" if env_choice == "railway" else ".env.local")

# Load environment variables
if not env_file.exists():
    raise FileNotFoundError(f"❌ ENV file not found → {env_file}")
load_dotenv(dotenv_path=env_file)

print(f"✅ Environment loaded from: {env_file.name} → ACTIVE_DB = {env_choice}")

# ========================== 🛢️ DATABASE URL ==============================
# Read the correct database URL from environment
DATABASE_URL = os.getenv(
    "RAILWAY_DATABASE_URL" if env_choice == "railway" else "LOCAL_DATABASE_URL"
)

if not DATABASE_URL:
    raise RuntimeError(
        f"❌ DATABASE_URL not found.\n"
        f"👉 Expected: {'RAILWAY_DATABASE_URL' if env_choice == 'railway' else 'LOCAL_DATABASE_URL'}"
    )

# ========================== ⚙️ SQLALCHEMY ENGINE =========================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # Auto-check DB connection
    echo=False            # Set to True to debug raw SQL queries
)

# ========================== 🧠 SESSION & BASE =============================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ========================== 🔁 FASTAPI DB DEPENDENCY ======================
def get_db():
    """
    Yields a database session for FastAPI routes, auto-closes after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
