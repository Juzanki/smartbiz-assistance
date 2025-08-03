"""
Authentication & User Management Routes
Includes signup, login, profile update, subscription-based features.
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.dependencies import require_plan
from backend.schemas import PostCreate, PostOut, UserCreate, UserUpdate, User, Token
from backend.crud.user_crud import (
    get_user_by_email,
    create_user,
    update_user_profile,
    get_user_posts,
)
from backend.auth import (
    get_current_user,
    authenticate_user,
    get_db,
)
from backend.utils.security import (
    get_password_hash,
    create_access_token,
)

router = APIRouter()
logging.basicConfig(level=logging.INFO)

# ========== CURRENT USER PROFILE ==========

@router.get("/auth/me", response_model=User)
def get_my_profile(current_user: User = Depends(get_current_user)):
    """Retrieve the current authenticated user's profile."""
    return current_user

# ========== USER SIGNUP ==========

@router.post("/auth/signup", response_model=User, status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user account."""
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    user.password = get_password_hash(user.password)
    return create_user(db=db, user=user)

# ========== USER LOGIN ==========
@router.post("/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate user and return JWT token, role, language, and name.
    """
    identifier = form_data.username.strip().lower()
    password = form_data.password.strip()
    logging.info(f"🔐 Login attempt from: {identifier}")

    user = authenticate_user(db, identifier=identifier, password=password)
    if not user:
        logging.warning(f"❌ Invalid login attempt for: {identifier}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your email/username/phone and password.",
        )

    access_token = create_access_token(data={"sub": user.email})
    logging.info(f"✅ Login successful: {user.email} ({user.role})")

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "name": user.full_name or user.username,
        "language": user.language or "en"
    }

# ========== UPDATE PROFILE ==========

@router.put("/auth/update-profile", response_model=User)
def update_profile(
    updated_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update current user's profile details."""
    return update_user_profile(db=db, user_id=current_user.id, updates=updated_user.dict())

# ========== CREATE POST (INACTIVE PLACEHOLDER) ==========

@router.post("/auth/create-post", response_model=PostOut)
def create_post(
    post_data: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_plan(["Pro", "Business"]))
):
    """
    Create a new post (only for Pro or Business plans).
    NOTE: This is a placeholder until Post model is implemented.
    """
    raise HTTPException(status_code=501, detail="Post creation not implemented yet.")

# ========== GET USER POSTS ==========

@router.get("/auth/my-posts", response_model=List[PostOut])
def list_my_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List all posts created by the current user."""
    return get_user_posts(db=db, user_id=current_user.id)

# ========== ACCESS PREMIUM CHATBOT ==========

@router.get("/auth/pro-chatbot")
def premium_chatbot_feature(current_user: User = Depends(require_plan(["Pro", "Business"]))):
    """Premium chatbot feature for Pro/Business subscribers."""
    return {
        "message": f"Welcome {current_user.full_name}, you now have access to the AI Premium Chatbot!",
        "feature": "Smart AI Auto-Responder"
    }

# ========== ACCESS FREE FEATURE ==========

@router.get("/auth/free-feature")
def free_feature(current_user: User = Depends(require_plan(["Free", "Pro", "Business"]))):
    """Free feature accessible to all subscription levels."""
    return {
        "message": f"Hello {current_user.full_name}, enjoy this free feature available to everyone!"
    }
