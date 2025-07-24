from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.post_live_notification_schemas import PostLiveNotificationOut
from backend.dependencies import get_db, get_current_user
from backend.models.user import User
from backend.crud import post_live_notification_crud

router = APIRouter()

@router.get("/", response_model=list[PostLiveNotificationOut])
def get_my_notifications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return post_live_notification_crud.get_user_notifications(db, current_user.id)
