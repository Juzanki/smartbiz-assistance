from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime

class ReplayActivityLog(Base):
    __tablename__ = "replay_activity_logs"

    id = Column(Integer, primary_key=True, index=True)
    video_post_id = Column(Integer, ForeignKey("video_posts.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String)  # "share" or "download"
    platform = Column(String, nullable=True)  # Optional: "whatsapp", "facebook"
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    video_post = relationship("VideoPost")
