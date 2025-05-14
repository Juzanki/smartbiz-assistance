# === backend/models/scheduled_message.py ===
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime


class ScheduledMessage(Base):
    __tablename__ = "scheduled_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    platform = Column(String, nullable=False)  # telegram, whatsapp, sms, etc.
    scheduled_time = Column(DateTime, nullable=False)
    sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="scheduled_messages")

    def __repr__(self):
        return (
            f"<ScheduledMessage(user_id={self.user_id}, platform='{self.platform}', sent={self.sent})>"
        )
