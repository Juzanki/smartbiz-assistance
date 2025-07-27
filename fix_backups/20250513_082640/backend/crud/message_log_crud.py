from datetime import datetime
from sqlalchemy.orm import Session
from backend.models import MessageLog

# --- Log Message ---
def log_message(db: Session, sender_id: str, sender_name: str, content: str, source: str = "telegram") -> MessageLog:
    log_entry = MessageLog(
        sender_id=sender_id,
        sender_name=sender_name,
        content=content,
        source=source,
        timestamp=datetime.utcnow()
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return log_entry
