from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.db import Base


class AdEarning(Base):
    __tablename__ = "ad_earnings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ad_type = Column(String, default="video")  # video, banner, sponsor
    smartcoins_earned = Column(Float, nullable=False)
    details = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="ad_earnings")
