from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class MagicLink(Base):
    """
    Stores secure, one-time login links for admin/owner access.
    Used for magic login via email with expiration and IP restriction.
    """
    __tablename__ = "magic_links"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    token = Column(String(255), unique=True, nullable=False)
    ip_address = Column(String(100), nullable=True)  # Optional restriction
    expires_at = Column(DateTime, nullable=False)
    used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="magic_links")

    def is_expired(self) -> bool:
        return datetime.utcnow() > self.expires_at

    def __repr__(self):
        return (
            f"<MagicLink(user_id={self.user_id}, used={self.used}, expires_at={self.expires_at})>"
        )
