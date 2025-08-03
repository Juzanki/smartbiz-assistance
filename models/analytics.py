from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class AnalyticsSnapshot(Base):
    """
    Stores daily or periodic summary stats per user for dashboard display.
    """
    __tablename__ = "analytics_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    snapshot_time = Column(DateTime, default=datetime.utcnow, index=True)

    messages_sent = Column(Integer, default=0)
    messages_received = Column(Integer, default=0)
    active_platforms = Column(Integer, default=0)
    response_rate = Column(Float, default=0.0)         # Percentage like 89.5
    engagement_score = Column(Float, default=0.0)      # Calculated score for future analysis

    # Relationship to User
    user = relationship("User", back_populates="analytics_snapshots")

    def __repr__(self):
        return (
            f"<AnalyticsSnapshot(id={self.id}, user_id={self.user_id}, "
            f"time={self.snapshot_time.date()}, sent={self.messages_sent}, received={self.messages_received})>"
        )
