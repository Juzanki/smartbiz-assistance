from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class CoHost(Base):
    __tablename__ = "co_hosts"

    id = Column(Integer, primary_key=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, default="pending")  # pending, accepted, removed
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    stream = relationship("LiveStream", back_populates="cohosts")
    user = relationship("User", back_populates="co_host_entries")
