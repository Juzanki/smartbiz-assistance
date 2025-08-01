"""
?? SmartBiz Assistance: PostgreSQL Database Configuration
-------------------------------------------------------------
?? Securely loads environment variables from `.env.local` or `.env.production`
?? Initializes SQLAlchemy engine, session, and declarative base for ORM
"""

import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ============================ ?? BASE DIRECTORY ============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================ ?? ENV SWITCHING =============================
# Detect active environment: 'railway' (production) or 'local' (development)
ACTIVE_DB = os.getenv("ACTIVE_DB", "local").strip().lower()

# Load .env file safely

print(f"? Environment Loaded ? ACTIVE_DB = {ACTIVE_DB}")

# ============================ ?? DATABASE URL ==============================
# Load appropriate DATABASE_URL based on environment
DATABASE_URL = os.getenv(
    "RAILWAY_DATABASE_URL" if ACTIVE_DB == "railway" else "LOCAL_DATABASE_URL"
)

if not DATABASE_URL:
    raise RuntimeError(
        f"? DATABASE_URL not found.\n?? Expected: "
        f"{'RAILWAY_DATABASE_URL' if ACTIVE_DB == 'railway' else 'LOCAL_DATABASE_URL'}"
    )

# ============================ ?? DATABASE ENGINE ===========================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Auto-check connection health
    echo=False           # Set to True to enable SQL log output
)

# ============================ ?? SESSION CREATION ==========================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ============================ ?? DECLARATIVE BASE ==========================
Base = declarative_base()

# Optional: Auto-create tables (can be removed in production)
# from your_models_module import *   # Replace with actual models file
# Base.metadata.create_all(bind=engine)

# ============================ ?? DB DEPENDENCY FOR FASTAPI =================
def get_db():
    """
    Provides a SQLAlchemy session for FastAPI routes.
    Ensures automatic closing of DB session after request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
