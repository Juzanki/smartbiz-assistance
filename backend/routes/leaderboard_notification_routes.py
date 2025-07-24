from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.leaderboard_notification import LeaderboardNotification
from backend.schemas.leaderboard_notification_schemas import LeaderboardNotificationOut

router = APIRouter()

@router.get("/stream/{stream_id}/user/{user_id}", response_model=list[LeaderboardNotificationOut])
def get_user_notifications(stream_id: int, user_id: int, db: Session = Depends(get_db)):
    return db.query(LeaderboardNotification).filter_by(stream_id=stream_id, user_id=user_id).order_by(LeaderboardNotification.created_at.desc()).all()

@router.post("/mark-seen/{notification_id}")
def mark_notification_seen(notification_id: int, db: Session = Depends(get_db)):
    notif = db.query(LeaderboardNotification).filter_by(id=notification_id).first()
    if notif:
        notif.seen = True
        db.commit()
    return {"message": "Marked as seen"}
