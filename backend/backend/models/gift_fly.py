from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from backend.db import Base
from datetime import datetime

class GiftFly(Base):
    __tablename__ = "gift_fly_events"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    gift_name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # 🔁 Relationships
    stream = relationship("LiveStream", back_populates="gift_fly_events")
    user = relationship("User", back_populates="gift_fly_events")  # Hakikisha upande wa User una backref: gift_fly_events
