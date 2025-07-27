from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.db import Base


class UserDevice(Base):
    """
    Tracks login devices and IPs per user for security and device management.
    Useful for suspicious activity detection and limiting device access.
    """
    __tablename__ = "user_devices"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    device_type = Column(String(100), nullable=True)   # e.g., Windows PC, iPhone, Android
    device_name = Column(String(100), nullable=True)
    ip_address = Column(String(100), nullable=True)
    location = Column(String(100), nullable=True)       # optional: based on IP
    is_trusted = Column(Boolean, default=False)
    last_active = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="user_devices")

    def __repr__(self):
        return f"<UserDevice(user_id={self.user_id}, device='{self.device_name}', trusted={self.is_trusted})>"
