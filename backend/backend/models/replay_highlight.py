from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime

class ReplayHighlight(Base):
    __tablename__ = "replay_highlights"

    id = Column(Integer, primary_key=True, index=True)
    video_post_id = Column(Integer, ForeignKey("video_posts.id"), nullable=False)
    title = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)  # Format: HH:MM:SS
    created_at = Column(DateTime, default=datetime.utcnow)

    video_post = relationship("VideoPost", back_populates="highlights")
