from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import MessageLog, User
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/inbox", tags=["Inbox"])


# ========== Schema ==========
class MessageOut(BaseModel):
    id: int
    sender_name: str
    message: str
    platform: str
    chat_id: str
    received_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "sender_name": "John Doe",
                "message": "Hello, I need help with my order",
                "platform": "telegram",
                "chat_id": "123456789",
                "received_at": "2025-05-13T12:34:56"
            }
        }


# ========== GET Messages ==========
@router.get("/", response_model=List[MessageOut], summary="📥 Get messages in inbox")
def get_all_messages(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Return all messages:
    - Admin/Owner: See all
    - Normal User: See only their chat messages
    """
    if current_user.role in ['admin', 'owner']:
        messages = db.query(MessageLog).order_by(
            MessageLog.received_at.desc()).all()
    else:
        messages = db.query(MessageLog).filter(
            MessageLog.chat_id == str(current_user.id)
        ).order_by(MessageLog.received_at.desc()).all()

    return messages
