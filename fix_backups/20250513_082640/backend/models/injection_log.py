# backend/models/injection_log.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from backend.db import Base


class InjectionLog(Base):
    """
    InjectionLog model — stores log entries of AI-injected code actions (success/failure).
    Useful for auditing SmartInjectGPT behavior.
    """
    __tablename__ = "injection_logs"

    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String(100), index=True)
    content = Column(Text, nullable=False)
    status = Column(String(20), default="success")  # success or failed
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<InjectionLog(tag='{self.tag}', status='{self["status"]', time='{self.timestamp}')>"
