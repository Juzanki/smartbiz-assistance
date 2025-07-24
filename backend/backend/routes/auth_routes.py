"""
Auth Routes for SmartBiz Assistant.
Handles login, registration, password reset, and session verification.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from pydantic import BaseModel, EmailStr, Field

from backend.db import get_db
from backend.models import User
from backend.utils.security import verify_password, get_password_hash
from backend.auth import create_access_token, get_current_user

router = APIRouter(tags=["Authentication"])


# ==================== Schemas ====================

class LoginOutput(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


class RegisterInput(BaseModel):
    username: str = Field(..., min_length=3, example="johndoe")
    email: EmailStr
    phone_number: str = Field(..., min_length=10, example="+255712345678")
    full_name: str = Field(..., example="John Doe")
    password: str = Field(..., min_length=6)


class MeResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: str
    subscription_status: str

    class Config:
        from_attributes = True


# ==================== LOGIN ====================

@router.post("/login", response_model=LoginOutput, summary="🔐 Login using email, phone or username")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate a user by email, username, or phone number and return a JWT token.
    """
    identifier = form_data.username.strip().lower()

    user = db.query(User).filter(
        or_(
            func.lower(User.email) == identifier,
            func.lower(User.username) == identifier,
            func.lower(User.phone_number) == identifier
        )
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials: user not found"
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials: incorrect password"
        )

    if not getattr(user, "is_active", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Your account is inactive. Please contact support."
        )

    token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "role": getattr(user, "role", "user"),
            "language": getattr(user, "language", "en"),
            "subscription_status": user.subscription_status,
        }
    }


# ==================== REGISTER ====================

@router.post("/register", summary="📝 Register a new user")
def register(data: RegisterInput, db: Session = Depends(get_db)):
    """
    Create a new user account. Ensures email, phone, and username uniqueness.
    """
    duplicate = db.query(User).filter(
        or_(
            func.lower(User.email) == data.email.lower(),
            func.lower(User.username) == data.username.lower(),
            func.lower(User.phone_number) == data.phone_number.lower()
        )
    ).first()

    if duplicate:
        raise HTTPException(
            status_code=400,
            detail="User with same email, phone, or username already exists."
        )

    user = User(
        username=data.username.strip(),
        email=data.email.strip(),
        phone_number=data.phone_number.strip(),
        full_name=data.full_name.strip(),
        password=get_password_hash(data.password),
        subscription_status="free",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "✅ Registration successful", "user_id": user.id}


# ==================== PROFILE ====================

@router.get("/me", response_model=MeResponse, summary="👤 Get current user profile")
def get_profile(current_user: User = Depends(get_current_user)):
    """
    Retrieve details of the currently authenticated user.
    """
    return current_user
