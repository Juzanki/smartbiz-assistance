# === backend/models/message_log.py ===
from sqlalchemy import Column, Integer, String, Text, DateTime
from backend.db import Base
from datetime import datetime

class MessageLog(Base):
    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String)
    sender_name = Column(String)
    content = Column(Text)
    source = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

