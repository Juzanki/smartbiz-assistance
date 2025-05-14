# backend/models/message.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class MessageLog(Base):
    """
    MessageLog model — stores incoming messages for analytics and review.
    """
    __tablename__ = "message_logs"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, index=True, nullable=False)
    sender = Column(String, default="user")
    username = Column(String, nullable=True)
    message = Column(Text, nullable=False)
    received_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        short_msg = (self.message[:30] + '...') if len(self.message) > 30 else self.message
        return f"<MessageLog(chat_id={self.chat_id}, message='{short_msg}')>"


class ScheduledMessage(Base):
    """
    ScheduledMessage model — stores messages scheduled to be sent later.
    """
    __tablename__ = "scheduled_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    platform = Column(String, nullable=False)  # e.g., telegram, whatsapp, sms
    recipient = Column(String, nullable=False)  # phone or chat_id
    scheduled_time = Column(DateTime, nullable=False)
    sent = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="scheduled_messages")

    def __repr__(self):
        return f"<ScheduledMessage(to='{self.recipient}', time='{self.scheduled_time}')>"
