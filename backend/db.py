"""
Database configuration and session management for SmartBiz SaaS backend.
Loads environment variables and sets up SQLAlchemy with PostgreSQL.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables from .env.production (for Render)
load_dotenv(".env.production")

# Get full DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Safety check
if not DATABASE_URL:
    raise ValueError("⚠️ 'DATABASE_URL' environment variable is missing. Check .env.production file.")

# Initialize SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare base for models
Base = declarative_base()

# Dependency to get a database session
def get_db():
    """FastAPI dependency to provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
