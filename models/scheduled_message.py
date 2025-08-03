# === backend/models/scheduled_message.py ===
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime


class ScheduledMessage(Base):
    __tablename__ = "scheduled_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    recipient = Column(String, nullable=False, index=True)  # e.g. phone number or chat_id
    content = Column(Text, nullable=False)
    platform = Column(String, nullable=False)  # telegram, whatsapp, sms, etc.

    scheduled_time = Column(DateTime, nullable=False, index=True)
    sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="scheduled_messages")

    def __repr__(self):
        return (
            f"<ScheduledMessage(id={self.id}, user_id={self.user_id}, platform='{self.platform}', "
            f"recipient='{self.recipient}', scheduled_time='{self.scheduled_time}', sent={self.sent})>"
        )
