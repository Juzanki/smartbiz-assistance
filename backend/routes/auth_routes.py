"""
Auth Routes for SmartBiz Assistant.
Handles login, registration, password reset, and session verification.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
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
    phone_number: str = Field(..., example="+255712345678")
    full_name: str = Field(..., example="John Doe")
    password: str = Field(..., min_length=6)


class MeResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    subscription_status: str


# ==================== LOGIN ====================

@router.post("/login", response_model=LoginOutput, summary="🔐 Login using email, phone or username")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate a user by email, username, or phone number and return a JWT token.
    """
    user = db.query(User).filter(
        (User.email == form_data.username) |
        (User.username == form_data.username) |
        (User.phone_number == form_data.username)
    ).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email/username/phone or password"
        )

    token = create_access_token(data={"sub": user.email})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "full_name": user.full_name,
            "role": user.role,
            "language": user.language,
            "subscription_status": user.subscription_status,
        }
    }

# ==================== REGISTER ====================

@router.post("/register", summary="📝 Register a new user")
def register(data: RegisterInput, db: Session = Depends(get_db)):
    """
    Create a new user account. Ensures email and username uniqueness.
    """
    existing_user = db.query(User).filter(
        (User.email == data.email) | (User.username == data.username)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User with same email or username already exists.")

    new_user = User(
        username=data.username,
        email=data.email,
        phone_number=data.phone_number,
        full_name=data.full_name,
        password=get_password_hash(data.password),
        subscription_status="free",
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "✅ Registration successful", "user_id": new_user.id}


# ==================== PROFILE ====================

@router.get("/me", response_model=MeResponse, summary="👤 Get current user profile")
def get_profile(current_user: User = Depends(get_current_user)):
    """
    Retrieve details of the currently authenticated user.
    """
    return current_user
