from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import Settings, User
from backend.schemas import SettingsCreate, SettingsOut
from backend.dependencies import get_current_user

router = APIRouter(prefix="/settings", tags=["Settings"])


# ================= GET USER SETTINGS =================
@router.get("/me", response_model=SettingsOut, summary="⚙️ Get current user settings")
def get_user_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    settings = db.query(Settings).filter(Settings.user_id == current_user.id).first()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings


# ================= CREATE SETTINGS =================
@router.post("/create", response_model=SettingsOut, status_code=status.HTTP_201_CREATED, summary="➕ Create settings for user")
def create_user_settings(
    payload: SettingsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = db.query(Settings).filter(Settings.user_id == current_user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Settings already exist for this user.")

    new_settings = Settings(user_id=current_user.id, **payload.dict())
    db.add(new_settings)
    db.commit()
    db.refresh(new_settings)
    return new_settings


# ================= UPDATE SETTINGS =================
@router.put("/update", response_model=SettingsOut, summary="✏️ Update user settings")
def update_user_settings(
    payload: SettingsCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    settings = db.query(Settings).filter(Settings.user_id == current_user.id).first()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")

    update_data = payload.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(settings, field, value)

    db.commit()
    db.refresh(settings)
    return settings
