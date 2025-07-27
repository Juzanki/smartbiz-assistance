from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class AutoReplyTraining(Base):
    """
    Stores custom keyword-based training data per user to guide auto-replies.
    e.g., "Habari" → "Karibu SmartBiz, naweza kukusaidia vipi?"
    """
    __tablename__ = "auto_reply_training"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    keyword = Column(String(100), nullable=False)
    reply = Column(Text, nullable=False)
    platform = Column(String(50), default="all")  # whatsapp, telegram, sms, all
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="auto_reply_training")

    def __repr__(self):
        return f"<AutoReplyTraining(user_id={self.user_id}, keyword='{self.keyword}')>"
