# backend/models/connected_platform.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class ConnectedPlatform(Base):
    """
    ConnectedPlatform model — represents social/media platforms linked to a user account.
    Examples include: Telegram, WhatsApp, SMS, Facebook.
    """
    __tablename__ = "connected_platforms"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)
    platform = Column(String(50), nullable=False)  # telegram, whatsapp, sms
    access_token = Column(String, nullable=False)
    connected_at = Column(DateTime, default=datetime.utcnow)
    preferred_language = Column(String(10), default="en")

    user = relationship("User", back_populates="platforms")

    def __repr__(self):
        return f"<ConnectedPlatform(user_id={self.user_id}, platform='{self["platform"]}')>"
