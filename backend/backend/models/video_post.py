from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

from backend.models.replay_highlight import ReplayHighlight
from backend.models.video_comment import VideoComment
from backend.models.recorded_stream import RecordedStream
from backend.models.view_stat import VideoViewStat


class VideoPost(Base):
    __tablename__ = "video_posts"

    id = Column(Integer, primary_key=True, index=True)
    recorded_stream_id = Column(Integer, ForeignKey("recorded_streams.id", ondelete="CASCADE"), nullable=False)
    caption = Column(String, nullable=True)
    hashtags = Column(String, nullable=True)
    is_draft = Column(Boolean, default=True)
    video_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    recorded_stream = relationship("RecordedStream", back_populates="video_post")
    highlights = relationship("ReplayHighlight", back_populates="video_post", cascade="all, delete-orphan")
    comments = relationship("VideoComment", back_populates="video_post", cascade="all, delete-orphan")
    view_stats = relationship("VideoViewStat", back_populates="video_post", cascade="all, delete-orphan")

