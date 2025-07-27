from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class ReferralBonus(Base):
    """
    Tracks referral rewards earned by users when they invite others.
    Useful for incentive and growth systems.
    """
    __tablename__ = "referral_bonuses"

    id = Column(Integer, primary_key=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users["id"]), nullable=False)
    referred_user_id = Column(Integer, ForeignKey("users["id"]), nullable=False)

    reward_type = Column(String(50), default="cash")  # cash, points, gift
    reward_value = Column(Float, default=0.0)
    status = Column(String(20), default="pending")  # pending, approved, paid
    awarded_at = Column(DateTime, default=datetime.utcnow)

    referrer = relationship("User", foreign_keys=[referrer_id], back_populates="referral_bonuses")
    referred = relationship("User", foreign_keys=[referred_user_id])

    def __repr__(self):
        return f"<ReferralBonus(referrer_id={self.referrer_id}, reward={self.reward_value}, status={self["status"])>"
