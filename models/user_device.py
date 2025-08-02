# === backend/models/user_device.py ===

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class UserDevice(Base):
    """
    Represents a user's device and its metadata for tracking login sessions.
    """
    __tablename__ = "user_devices"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    device_type = Column(String(100))  # e.g., 'Android', 'iPhone', 'Web'
    device_info = Column(String(255))  # e.g., 'Chrome on Windows 10'
    ip_address = Column(String(100))
    last_active = Column(DateTime, default=datetime.utcnow)

    # 🔁 Relationship to User model
    user = relationship("User", back_populates="user_devices")

    def __repr__(self):
        return (
            f"<UserDevice(user_id={self.user_id}, device='{self.device_type}', "
            f"last_active={self.last_active})>"
        )
