from datetime import datetime
from sqlalchemy.orm import Session
from typing import List
from backend.models import ScheduledMessage
from backend.schemas.scheduled import ScheduledMessageCreate

# --- Create Scheduled Message ---
def create_scheduled_message(db: Session, user_id: int, msg: ScheduledMessageCreate) -> ScheduledMessage:
    new_msg = ScheduledMessage(**msg.dict(), user_id=user_id)
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return new_msg

# --- Get User Scheduled Messages ---
def get_user_scheduled_messages(db: Session, user_id: int) -> List[ScheduledMessage]:
    return db.query(ScheduledMessage).filter(ScheduledMessage.user_id == user_id).order_by(ScheduledMessage.scheduled_time.desc()).all()

# --- Get Due Unsent Messages ---
def get_due_unsent_messages(db: Session) -> List[ScheduledMessage]:
    now = datetime.utcnow()
    return db.query(ScheduledMessage).filter(ScheduledMessage.sent == False, ScheduledMessage.scheduled_time <= now).all()

# --- Mark Message as Sent ---
def mark_as_sent(db: Session, msg: ScheduledMessage):
    msg.sent = True
    db.commit()
    db.refresh(msg)
