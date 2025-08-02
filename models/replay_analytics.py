from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime

class ReplayAnalytics(Base):
    __tablename__ = "replay_analytics"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id", ondelete="CASCADE"), nullable=False)
    metric = Column(String, nullable=False)  # e.g., 'views', 'likes', 'comments'
    value = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔁 Link to parent stream
    stream = relationship("LiveStream", back_populates="analytics_entries")
