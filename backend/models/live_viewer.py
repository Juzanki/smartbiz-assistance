from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class LiveViewer(Base):
    __tablename__ = "live_viewers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
    left_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

    user = relationship("User")
    stream = relationship("LiveStream", back_populates="viewers")
