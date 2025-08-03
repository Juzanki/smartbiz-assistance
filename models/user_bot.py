# backend/models/user_bot.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class UserBot(Base):
    """
    UserBot model — Represents an AI bot instance owned by a user.
    Links the bot to a specific user and subscription package.
    """
    __tablename__ = "user_bots"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    purpose = Column(Text, nullable=True)
    bot_package_id = Column(Integer, ForeignKey("bot_packages.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔁 Relationships
    user = relationship("User", back_populates="bots")
    package = relationship("BotPackage", back_populates="bots")

    def __repr__(self):
        return f"<UserBot(id={self.id}, name='{self.name}', user_id={self.user_id}, active={self.is_active})>"
