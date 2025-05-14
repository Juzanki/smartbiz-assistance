import asyncio
from datetime import datetime

from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.crud.user_crud import get_due_unsent_messages, mark_as_sent
from backend.utils.telegram_bot import send_telegram_message
from backend.utils.whatsapp import send_whatsapp_message
from backend.utils.sms import send_sms_message


async def run_scheduled_task():
    while True:
        try:
            db: Session = SessionLocal()
            due_messages = get_due_unsent_messages(db)

            for msg in due_messages:
                platform = getattr(msg, "platform", None)
                recipient = getattr(msg, "recipient", None)
                content = getattr(msg, "message", "")

                if not platform or not recipient:
                    print(f"⚠️ Skipping invalid message (missing platform or recipient): {msg}")
                    continue

                if platform == "telegram":
                    send_telegram_message(recipient, content)
                elif platform == "whatsapp":
                    send_whatsapp_message(recipient, content)
                elif platform == "sms":
                    send_sms_message(recipient, content)
                else:
                    print(f"⚠️ Unknown platform: {platform}")
                    continue

                mark_as_sent(db, msg)

            db.close()

        except Exception as e:
            print(f"[Scheduler error]: {e}")

        await asyncio.sleep(60)
