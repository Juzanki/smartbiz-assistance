from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class GiftMarker(Base):
    __tablename__ = "gift_markers"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    gift_name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    position = Column(Integer, default=0)

    # Relationships
    stream = relationship("LiveStream", back_populates="gift_markers")
