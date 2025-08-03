from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.auth import get_current_user
from backend.db import get_db
from backend.models import User
from backend.schemas import BroadcastMessage
from backend.dependencies import check_admin
from backend.utils.telegram_bot import send_telegram_message
# future: from backend.utils.whatsapp_bot import send_whatsapp_message
# future: from backend.utils.sms_gateway import send_sms

router = APIRouter(tags=["Broadcasts"])


@router.post("/broadcast", summary="📢 Send broadcast message to all users")
async def broadcast_message(
    payload: BroadcastMessage,
    db: Session = Depends(get_db),
    current_user: User = Depends(check_admin)
):
    """
    Send a broadcast message to all users through selected channels (Telegram, WhatsApp, SMS).
    Requires admin access.
    """
    if not payload.message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message content cannot be empty."
        )

    if not payload.channels:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one channel must be selected."
        )

    users = db.query(User).all()
    telegram_sent = 0
    # whatsapp_sent = 0
    # sms_sent = 0

    for user in users:
        if "telegram" in payload.channels and user.telegram_id:
            try:
                await send_telegram_message(user.telegram_id, payload.message)
                telegram_sent += 1
            except Exception as e:
                # Optional: log individual failure
                continue

        # if "whatsapp" in payload.channels and user.phone_number:
        #     try:
        #         await send_whatsapp_message(user.phone_number, payload.message)
        #         whatsapp_sent += 1
        #     except:
        #         continue

        # if "sms" in payload.channels and user.phone_number:
        #     try:
        #         await send_sms(user.phone_number, payload.message)
        #         sms_sent += 1
        #     except:
        #         continue

    return {
        "message": "✅ Broadcast completed",
        "total_users": len(users),
        "channels_used": payload.channels,
        "results": {
            "telegram": telegram_sent,
            # "whatsapp": whatsapp_sent,
            # "sms": sms_sent,
        }
    }
