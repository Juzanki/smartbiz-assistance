from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.gift_marker import GiftMarker
from backend.schemas.gift_marker_schemas import GiftMarkerCreate, GiftMarkerOut
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=GiftMarkerOut)
def create_gift_marker(marker: GiftMarkerCreate, db: Session = Depends(get_db)):
    new_marker = GiftMarker(
        stream_id=marker.stream_id,
        gift_name=marker.gift_name,
        position=marker.position,
        timestamp=datetime.utcnow()
    )
    db.add(new_marker)
    db.commit()
    db.refresh(new_marker)
    return new_marker

@router.get("/{stream_id}", response_model=list[GiftMarkerOut])
def get_gift_markers(stream_id: int, db: Session = Depends(get_db)):
    return db.query(GiftMarker).filter_by(stream_id=stream_id).order_by(GiftMarker.timestamp).all()
