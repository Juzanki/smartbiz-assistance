# backend/models/loyalty.py

from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class LoyaltyPoint(Base):
    """
    LoyaltyPoint model — tracks reward points earned by users based on actions.
    Useful for gift programs, gamification, or cashback.
    """
    __tablename__ = "loyalty_points"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)
    points = Column(Float, default=0.0)
    reason = Column(String(255), nullable=True)  # e.g., "Purchase", "Referral", "Promo Bonus"
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="loyalty_points")

    def __repr__(self):
        return f"<LoyaltyPoint(user_id={self.user_id}, points={self.points})>"
