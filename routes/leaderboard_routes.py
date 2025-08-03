from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from backend.db import get_db
from backend.models.gift_movement import GiftMovement

router = APIRouter()

@router.get("/daily/{stream_id}")
def daily_leaderboard(stream_id: int, db: Session = Depends(get_db)):
    today = datetime.utcnow().date()
    tomorrow = today + timedelta(days=1)

    results = (
        db.query(
            GiftMovement.sender_id,
            func.sum(GiftMovement.total_value).label("total_value")
        )
        .filter(
            GiftMovement.stream_id == stream_id,
            GiftMovement.sent_at >= today,
            GiftMovement.sent_at < tomorrow
        )
        .group_by(GiftMovement.sender_id)
        .order_by(func.sum(GiftMovement.total_value).desc())
        .limit(10)
        .all()
    )
    return results

@router.get("/weekly/{stream_id}")
def weekly_leaderboard(stream_id: int, db: Session = Depends(get_db)):
    start_date = datetime.utcnow().date() - timedelta(days=7)
    end_date = datetime.utcnow().date() + timedelta(days=1)

    results = (
        db.query(
            GiftMovement.sender_id,
            func.sum(GiftMovement.total_value).label("total_value")
        )
        .filter(
            GiftMovement.stream_id == stream_id,
            GiftMovement.sent_at >= start_date,
            GiftMovement.sent_at < end_date
        )
        .group_by(GiftMovement.sender_id)
        .order_by(func.sum(GiftMovement.total_value).desc())
        .limit(10)
        .all()
    )
    return results
