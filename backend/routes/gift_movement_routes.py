from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.gift_movement import GiftMovement
from backend.schemas.gift_movement_schemas import GiftMovementCreate
from datetime import datetime

router = APIRouter()

@router.post("/send")
def send_gift(data: GiftMovementCreate, db: Session = Depends(get_db)):
    movement = GiftMovement(**data.dict(), sent_at=datetime.utcnow())
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return {"message": "Gift sent", "movement_id": movement.id}

@router.get("/stream/{stream_id}")
def get_gift_movements(stream_id: int, db: Session = Depends(get_db)):
    gifts = db.query(GiftMovement).filter(GiftMovement.stream_id == stream_id).order_by(GiftMovement.sent_at.desc()).limit(50).all()
    return gifts
