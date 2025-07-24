from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.db import Base


class ReferralBonus(Base):
    __tablename__ = "referral_bonuses"

    id = Column(Integer, primary_key=True, index=True)
    referrer_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    bonus_name = Column(String, nullable=False)
    bonus_amount = Column(Integer, nullable=False)

    # Relationship
    referrer = relationship("User", back_populates="referral_bonuses")

    def __repr__(self):
        return f"<ReferralBonus(referrer_id={self.referrer_id}, bonus_name='{self.bonus_name}', bonus_amount={self.bonus_amount})>"
