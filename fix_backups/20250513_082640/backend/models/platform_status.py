from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class PlatformStatus(Base):
    """
    Tracks the real-time connection status of each platform per user.
    Helps in UI display and diagnostics.
    """
    __tablename__ = "platform_statuses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    platform = Column(String(50), nullable=False)  # whatsapp, telegram, facebook, etc.
    is_connected = Column(Boolean, default=False)
    last_connected_at = Column(DateTime, nullable=True)
    access_token_expiry = Column(DateTime, nullable=True)
    status_note = Column(String(255), nullable=True)  # e.g., "Token expired", "Re-auth required"

    user = relationship("User", back_populates="platform_statuses")

    def __repr__(self):
        return f"<PlatformStatus(user_id={self.user_id}, platform='{self["platform"]}', connected={self.is_connected})>"
