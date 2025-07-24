from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.schemas.notification import NotificationCreate, NotificationOut
from backend.crud import notification_crud
from backend.auth import get_current_user
from backend.models.user import User

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.post("/", response_model=NotificationOut)
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only allow admin or system to create for others
    if current_user.id != notification.user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized to send notifications to others")
    return notification_crud.create_notification(db, notification)

@router.get("/", response_model=List[NotificationOut])
def get_my_notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 20
):
    return notification_crud.get_user_notifications(db, user_id=current_user.id, skip=skip, limit=limit)

@router.put("/{notif_id}/read", response_model=NotificationOut)
def mark_as_read(
    notif_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    notif = notification_crud.mark_notification_as_read(db, notif_id)
    if not notif:
        raise HTTPException(status_code=404, detail="Notification not found")
    if notif.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your notification")
    return notif
