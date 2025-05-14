# backend/models/ai_bot_settings.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from backend.db import Base


class AIBotSettings(Base):
    """
    AIBotSettings model — stores AI assistant preferences per user.
    Includes greeting message, language, and allowed platforms.
    """
    __tablename__ = "ai_bot_settings"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    active = Column(Boolean, default=True)
    language = Column(String(10), default="en")
    default_greeting = Column(
        String(255),
        default="Hello! How can I assist you today?"
    )
    platforms = Column(JSON, default=list)  # e.g. ["telegram", "whatsapp"]

    user = relationship("User", back_populates="ai_bot_settings")

    def __repr__(self):
        return f"<AIBotSettings(user_id={self.user_id}, language='{self.language}')>"
