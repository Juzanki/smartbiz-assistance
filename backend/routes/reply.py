from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from enum import Enum
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import User

from backend.utils.telegram_bot import send_telegram_message
from backend.utils.whatsapp import send_whatsapp_message
from backend.utils.sms import send_sms_message

router = APIRouter(prefix="/messages", tags=["Replies"])


# ========== Enums & Schemas ==========
class PlatformType(str, Enum):
    telegram = "telegram"
    whatsapp = "whatsapp"
    sms = "sms"


class ReplyRequest(BaseModel):
    chat_id: str = Field(..., example="1234567890")
    platform: PlatformType
    message: str = Field(..., example="Hello! How can I help you?")


class ReplyResponse(BaseModel):
    message: str
    platform: PlatformType
    result: str


# ========== Endpoint ==========
@router.post("/send-reply", response_model=ReplyResponse, summary="📨 Send Reply to User")
def send_reply(
    payload: ReplyRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Send a reply to a user via Telegram, WhatsApp, or SMS.
    """

    try:
        if payload.platform == PlatformType.telegram:
            res = send_telegram_message(chat_id=payload.chat_id, message=payload.message)
        elif payload.platform == PlatformType.whatsapp:
            res = send_whatsapp_message(phone=payload.chat_id, message=payload.message)
        elif payload.platform == PlatformType.sms:
            res = send_sms_message(phone=payload.chat_id, message=payload.message)
        else:
            raise ValueError("Unsupported platform")

        return ReplyResponse(
            message="✅ Reply sent successfully",
            platform=payload.platform,
            result=res
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send reply: {str(e)}"
        )
