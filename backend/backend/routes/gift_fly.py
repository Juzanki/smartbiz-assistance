from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.gift_fly import GiftFly
from backend.schemas.gift_fly_schemas import GiftFlyCreate, GiftFlyOut
from backend.utils.websocket_manager import WebSocketManager
from datetime import datetime

router = APIRouter()
manager = WebSocketManager()

@router.post("/", response_model=GiftFlyOut)
async def send_gift(data: GiftFlyCreate, db: Session = Depends(get_db)):
    new_gift = GiftFly(
        stream_id=data.stream_id,
        user_id=data.user_id,
        gift_name=data.gift_name,
        sent_at=datetime.utcnow()
    )
    db.add(new_gift)
    db.commit()
    db.refresh(new_gift)

    await manager.broadcast(data.stream_id, {
        "type": "gift_fly",
        "user_id": data.user_id,
        "gift_name": data.gift_name,
        "timestamp": str(new_gift.sent_at)
    })

    return new_gift
