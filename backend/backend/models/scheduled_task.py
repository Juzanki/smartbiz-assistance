from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class ScheduledTask(Base):
    __tablename__ = "scheduled_tasks"
    # Auto-added back_populates
    failure_logs = relationship("System.Collections.Hashtable.from", back_populates="ScheduledTask", cascade="all, delete-orphan")

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50), default="message")  # message, email, post, etc
    content = Column(String, nullable=False)
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String(20), default="pending")  # pending, running, sent, failed
    retry_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="scheduled_tasks")
