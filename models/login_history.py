from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class LoginHistory(Base):
    """
    Logs every login attempt for a user, including success/failure, IP, and device.
    Useful for security analytics, session tracking, and suspicious activity alerts.
    """
    __tablename__ = "login_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    ip_address = Column(String(100), nullable=True)
    device_type = Column(String(100), nullable=True)  # e.g., Mobile, PC, Tablet
    platform = Column(String(50), default="web")      # web, mobile, api, etc.
    successful = Column(Boolean, default=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="login_history")

    def __repr__(self):
        return (
            f"<LoginHistory(user_id={self.user_id}, ip='{self.ip_address}', success={self.successful})>"
        )
