from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base
import logging  # Hakikisha unatumia logging kwa ujumbe wa makosa

class PlatformStatus(Base):
    """
    Tracks the real-time connection status of each platform per user.
    Helps in UI display and diagnostics.
    """
    __tablename__ = "platform_statuses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # whatsapp, telegram, facebook, etc.
    platform = Column(String(50), nullable=False)
    is_connected = Column(Boolean, default=False)
    last_connected_at = Column(DateTime, nullable=True)
    access_token_expiry = Column(DateTime, nullable=True)
    # e.g., "Token expired", "Re-auth required"
    status_note = Column(String(255), nullable=True)

    user = relationship("User", back_populates="platform_statuses")

    def __repr__(self):
        return (
            f"<PlatformStatus(user_id={self.user_id}, platform='{self.platform}', connected={self.is_connected})>"
        )

def update_platform_status(user_id, platform, is_connected):
    if platform and is_connected is not None:
        status = PlatformStatus(user_id=user_id, platform=platform, is_connected=is_connected)
        db_session.add(status)
        db_session.commit()
    else:
        logging.warning("Invalid platform status detected!")

def send_scheduled_posts(messages):
    for message in messages:
        if not message['platform'] or not message['recipient']:
            logging.warning(f"Skipping invalid message: {message}")
            return  # Hapa tumetumia return badala ya continue
        # Furahia kutuma ujumbe valid
        send_message_to_platform(message)
