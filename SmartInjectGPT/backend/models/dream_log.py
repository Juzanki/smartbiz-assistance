from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from backend.db import Base

class DreamLog(Base):
    __tablename__ = "dream_logs"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    result = Column(Text)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
