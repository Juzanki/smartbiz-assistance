"""
Routes for managing user profile operations in SmartBiz Assistant.
Includes get, update, delete, and fanbase stats.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.auth import get_current_user
from backend.schemas.user import UserUpdate, UserOut as UserSchema
from backend.models import User as UserModel

router = APIRouter(prefix="/profile", tags=["User Profile"])


# ==================== GET CURRENT PROFILE ====================
@router.get("/me", response_model=UserSchema, summary="🙋 Get current user profile with stats")
def read_current_user(
    current_user: UserModel = Depends(get_current_user)
):
    """
    Retrieve the currently authenticated user's full profile,
    including follower stats, language, and linked business.
    """
    return current_user


# ==================== UPDATE CURRENT PROFILE ====================
@router.put("/me", response_model=UserSchema, summary="✏️ Update current user profile")
def update_current_user(
    update_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Update the current authenticated user's profile fields:
    full name, business info, language, telegram ID, etc.
    """
    persistent_user = db.merge(current_user)

    for attr in [
        "full_name", "business_name", "business_type",
        "language", "telegram_id"
    ]:
        value = getattr(update_data, attr, None)
        if value is not None:
            setattr(persistent_user, attr, value)

    db.commit()
    db.refresh(persistent_user)
    return persistent_user


# ==================== DELETE CURRENT PROFILE ====================
@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT, summary="🗑️ Delete current user profile")
def delete_current_user(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Delete the current authenticated user's account completely from the system.
    """
    persistent_user = db.merge(current_user)

    if not persistent_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    db.delete(persistent_user)
    db.commit()
    return  # No return body for 204
