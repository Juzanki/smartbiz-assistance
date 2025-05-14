"""
Route to handle business user registration in SmartBiz Assistant.
Ensures unique phone, username, email, and Telegram ID.
"""

from uuid import uuid4
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.models import User
from backend.utils.security import get_password_hash

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ========== Schemas ==========
class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone_number: str
    full_name: Optional[str] = "Guest"
    business_name: str
    business_type: str
    language: str
    telegram_id: Optional[int] = None


class RegisterResponse(BaseModel):
    user_token: str
    message: str


# ========== Endpoint ==========
@router.post("/register-user", response_model=RegisterResponse, summary="📝 Register a new business user")
def register_user(data: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new SmartBiz business user. Validates uniqueness of:
    - Phone number
    - Telegram ID (optional)
    - Email
    - Username
    """

    # Validate uniqueness
    if db.query(User).filter_by(username=data.username).first():
        raise HTTPException(status_code=400, detail="Username already exists.")
    if db.query(User).filter_by(email=data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered.")
    if db.query(User).filter_by(phone_number=data.phone_number).first():
        raise HTTPException(status_code=400, detail="Phone number already registered.")
    if data.telegram_id:
        if db.query(User).filter_by(telegram_id=data.telegram_id).first():
            raise HTTPException(status_code=400, detail="Telegram ID already registered.")

    # Generate user token
    token = str(uuid4())

    # Create user
    new_user = User(
        username=data.username,
        email=data.email,
        full_name=data.full_name or "Guest User",
        password=get_password_hash(data.password),
        telegram_id=data.telegram_id,
        business_name=data.business_name,
        business_type=data.business_type,
        language=data.language,
        phone_number=data.phone_number,
        user_token=token,
        subscription_status="free",
        subscription_expiry=datetime.utcnow(),
        created_at=datetime.utcnow()
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return RegisterResponse(
            user_token=token,
            message="✅ Business registered successfully."
        )
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Registration failed due to internal error."
        ) from exc
