# === backend/models/chat.py ===

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class ChatMessage(Base):
    """
    Represents a single chat message sent within a live stream room.
    """
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)  # Sender reference
    room_id = Column(String, index=True)  # Room/session identifier
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship back to User
    sender = relationship("User", back_populates="chat_messages")
