from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import ConnectedPlatform, User
from backend.schemas import PlatformConnectRequest, PlatformOut

router = APIRouter(prefix="/platforms", tags=["Integrations"])


# ========== Connect New Platform ==========
@router.post("/connect", response_model=PlatformOut, summary="🔗 Connect a platform (e.g. WhatsApp, Telegram)")
def connect_platform(
    payload: PlatformConnectRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Convert platform to lowercase for consistency
    platform_name = payload.platform.lower()

    # Check if already connected
    existing = db.query(ConnectedPlatform).filter_by(
        user_id=current_user.id, platform=platform_name
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Platform '{platform_name}' is already connected."
        )

    platform = ConnectedPlatform(
        user_id=current_user.id,
        platform=platform_name,
        access_token=payload.access_token
    )

    db.add(platform)
    db.commit()
    db.refresh(platform)
    return platform


# ========== List Connected Platforms ==========
@router.get("/", response_model=list[PlatformOut], summary="📋 List connected platforms for current user")
def list_connected_platforms(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    platforms = db.query(ConnectedPlatform).filter_by(user_id=current_user.id).all()
    return platforms
