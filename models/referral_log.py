from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base

class ReferralLog(Base):
    """
    ReferralLog model — tracks referrals made by users for reward or commission purposes.
    Includes information about referrer, referred user, and related product/purchase.
    """
    __tablename__ = "referral_logs"

    id = Column(Integer, primary_key=True, index=True)

    referrer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    referred_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    product_name = Column(String(100), nullable=True)
    buyer_name = Column(String(100), nullable=True)
    amount = Column(Integer, nullable=True)
    status = Column(String(20), default="pending")  # pending, paid, rejected

    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    referrer = relationship("User", foreign_keys=[referrer_id], back_populates="referrals")
    referred_user = relationship("User", foreign_keys=[referred_user_id], back_populates="referrals_received")

    def __repr__(self):
        return (
            f"<ReferralLog(id={self.id}, referrer_id={self.referrer_id}, referred_user_id={self.referred_user_id}, "
            f"product='{self.product_name}', amount={self.amount}, status='{self.status}')>"
        )
