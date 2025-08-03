from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class GiftMovement(Base):
    __tablename__ = "gift_movements"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    gift_id = Column(Integer, ForeignKey("gifts.id"), nullable=False)
    amount = Column(Integer, default=1)
    total_value = Column(Integer, nullable=False)  # coins
    sent_at = Column(DateTime, default=datetime.utcnow)

    # ✅ Relationship to Gift
    gift = relationship("Gift", back_populates="movements")
