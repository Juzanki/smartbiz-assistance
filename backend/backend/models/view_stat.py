from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class VideoViewStat(Base):
    __tablename__ = "video_view_stats"  # ✅ clear and specific

    id = Column(Integer, primary_key=True, index=True)
    video_post_id = Column(Integer, ForeignKey("video_posts.id", ondelete="CASCADE"), nullable=False)
    viewer_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # can be anonymous
    viewed_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    video_post = relationship("VideoPost", back_populates="view_stats")
    viewer = relationship("User", back_populates="video_views")  # ✅ better name than just 'user'
