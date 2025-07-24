from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.replay_events import ReplayEvent
from backend.schemas.replay_event_schemas import ReplayEventCreate
from datetime import datetime

router = APIRouter()

@router.post("/auto-gift-marker")
def add_gift_marker(data: ReplayEventCreate, db: Session = Depends(get_db)):
    new_event = ReplayEvent(
        stream_id=data.stream_id,
        content=data.content,
        timestamp=data.timestamp,
        event_type="gift_marker",
        created_at=datetime.utcnow()
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Gift marker added", "event_id": new_event.id}
