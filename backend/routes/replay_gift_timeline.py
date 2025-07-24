from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.gift_fly import GiftFly
from datetime import datetime

router = APIRouter()

@router.get("/replay/gift_timeline/{stream_id}")
def get_gift_timeline(stream_id: int, db: Session = Depends(get_db)):
    return [
        {
            "gift_name": g.gift_name,
            "timestamp": g.sent_at.isoformat(),
            "position": g.position
        }
        for g in db.query(GiftFly).filter_by(stream_id=stream_id).order_by(GiftFly.sent_at.asc()).all()
    ]
