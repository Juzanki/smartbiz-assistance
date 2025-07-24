from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models.smart_reply import SmartReply
from backend.schemas.smart_reply_schema import SmartReplyCreate, SmartReplyOut

router = APIRouter(prefix="/smart-replies", tags=["Smart Replies"])

@router.post("/", response_model=List[SmartReplyOut])
def set_smart_replies(data: SmartReplyCreate, db: Session = Depends(get_db)):
    # Futa zilizopo kwanza kwa room_id hiyo
    db.query(SmartReply).filter(SmartReply.room_id == data.room_id).delete()
    db.commit()

    # Ingiza mpya
    new_replies = [
        SmartReply(room_id=data.room_id, message=msg)
        for msg in data.replies
    ]
    db.add_all(new_replies)
    db.commit()

    return new_replies

@router.get("/{room_id}", response_model=List[SmartReplyOut])
def get_smart_replies(room_id: str, db: Session = Depends(get_db)):
    return db.query(SmartReply).filter(SmartReply.room_id == room_id).all()
