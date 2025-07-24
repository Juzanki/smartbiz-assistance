# ✅ backend/tasks/scheduler.py

import asyncio
from datetime import datetime
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler

from backend.db import SessionLocal
from backend.crud.user_crud import get_due_unsent_messages, mark_as_sent
from backend.utils.telegram_bot import send_telegram_message
from backend.utils.whatsapp import send_whatsapp_message
from backend.utils.sms import send_sms_message

from backend.tasks.badge_upgrade import run_badge_upgrade_task

# === Asynchronous Task: Send queued messages across platforms ===
async def run_scheduled_message_dispatch():
    while True:
        print(f"[📤 {datetime.now().isoformat()}] Checking for scheduled messages...")

        db: Session = SessionLocal()
        try:
            due_messages = get_due_unsent_messages(db)

            if not due_messages:
                print("[ℹ️] No scheduled messages found.")

            for msg in due_messages:
                platform = (msg.platform or "").lower()
                recipient = msg.recipient
                content = msg.message

                if not platform or not recipient:
                    print(f"⚠️ Skipped invalid message (missing data): {msg}")
                    continue

                try:
                    sent_successfully = False

                    if platform == "telegram":
                        sent_successfully = send_telegram_message(recipient, content)
                    elif platform == "whatsapp":
                        sent_successfully = send_whatsapp_message(recipient, content)
                    elif platform == "sms":
                        sent_successfully = send_sms_message(recipient, content)
                    else:
                        print(f"⚠️ Unknown platform: {platform}")
                        continue

                    if sent_successfully:
                        mark_as_sent(db, msg)
                        print(f"✅ Sent via {platform} to {recipient}")
                    else:
                        print(f"❌ Failed via {platform} to {recipient}")

                except Exception as send_error:
                    print(f"🚨 Error sending message to {recipient}: {send_error}")

            db.commit()

        except Exception as e:
            print(f"[Scheduler Error]: {e}")

        finally:
            db.close()

        await asyncio.sleep(60)  # Check again every 60 seconds


# === APScheduler: Run Badge Upgrade Task periodically ===
scheduler = BackgroundScheduler()

def start_schedulers():
    try:
        scheduler.add_job(
            func=run_badge_upgrade_task,
            trigger="interval",
            hours=12,
            id="badge_upgrade_job",
            name="Auto-upgrade user badges"
        )
        scheduler.start()
        print("[⏱] APScheduler started with badge upgrade task every 12 hours.")
    except Exception as e:
        print(f"❌ Failed to start APScheduler: {e}")
