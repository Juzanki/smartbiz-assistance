# === backend/models/scheduled_message.py ===
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from backend.db import Base
from datetime import datetime

class ScheduledMessage(Base):
    __tablename__ = "scheduled_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]))
    content = Column(Text)
    platform = Column(String)
    scheduled_time = Column(DateTime)
    sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
