from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class ActivityScore(Base):
    """
    AI-powered engagement rating for each user.
    Useful for insights, gamification, or loyalty bonuses.
    """
    __tablename__ = "activity_scores"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    score = Column(Float, default=0.0)  # 0–100 rating
    messages_sent = Column(Integer, default=0)
    platforms_connected = Column(Integer, default=0)
    response_rate = Column(Float, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="activity_score")

    def __repr__(self):
        return f"<ActivityScore(user_id={self.user_id}, score={self.score})>"
