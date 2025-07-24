from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class PostLog(Base):
    """
    Tracks auto-published posts from Social Media Bot (e.g. Telegram, WhatsApp, Instagram).
    Useful for history, failure analysis, and audit trails.
    """
    __tablename__ = "post_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # telegram, whatsapp, instagram, etc.
    platform = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(String(20), default="pending")  # pending, sent, failed
    error_message = Column(Text, nullable=True)

    sent_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="post_logs")

    def __repr__(self):
        return (
            f"<PostLog(user_id={self.user_id}, platform='{self.platform}', status='{self.status}')>"
        )
