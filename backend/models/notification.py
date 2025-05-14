# backend/models/notification.py

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class Notification(Base):
    """
    Notification model — stores alerts and updates sent to users.
    Can be triggered by system events like new order, reply, payment confirmation, etc.
    """
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # e.g., system, message, billing, alert
    type = Column(String(50), nullable=False)
    title = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")

    def __repr__(self):
        return (
            f"<Notification(user_id={self.user_id}, title='{self.title}', read={self.read})>"
        )
