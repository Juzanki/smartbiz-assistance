from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class AnalyticsSnapshot(Base):
    """
    Stores daily or periodic summary stats per user for dashboard display.
    """
    __tablename__ = "analytics_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    date = Column(DateTime, default=datetime.utcnow, index=True)
    messages_sent = Column(Integer, default=0)
    messages_received = Column(Integer, default=0)
    active_platforms = Column(Integer, default=0)
    response_rate = Column(Float, default=0.0)  # e.g., 89.5
    engagement_score = Column(Float, default=0.0)  # future use

    user = relationship("User", back_populates="analytics_snapshots")

    def __repr__(self):
        return (
            f"<AnalyticsSnapshot(user_id={self.user_id}, "
            f"date={self.date.date()}, sent={self.messages_sent})>"
        )
