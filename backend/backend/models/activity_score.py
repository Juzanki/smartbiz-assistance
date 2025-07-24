# === backend/models/activity_score.py ===
from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class ActivityScore(Base):
    """
    Tracks user engagement scores using AI-based metrics.
    Helps in analytics, gamification, rewards, and customer profiling.
    """
    __tablename__ = "activity_scores"

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )

    score = Column(Float, default=0.0, nullable=False)  # Range: 0 to 100
    messages_sent = Column(Integer, default=0, nullable=False)
    platforms_connected = Column(Integer, default=0, nullable=False)
    response_rate = Column(Float, default=0.0, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship with User
    user = relationship("User", back_populates="activity_score")

    def __repr__(self):
        return f"<ActivityScore(user_id={self.user_id}, score={self.score}, response_rate={self.response_rate})>"
