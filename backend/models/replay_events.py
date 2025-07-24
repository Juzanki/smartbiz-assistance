from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from backend.db import Base
from datetime import datetime

class ReplayEvent(Base):
    __tablename__ = "replay_events"

    id = Column(Integer, primary_key=True, index=True)
    video_post_id = Column(Integer, ForeignKey("video_posts.id"), nullable=False)
    event_type = Column(String)  # "like", "comment"
    content = Column(String, nullable=True)  # e.g. comment text or null for like
    timestamp = Column(String, nullable=False)  # HH:MM:SS
    created_at = Column(DateTime, default=datetime.utcnow)
