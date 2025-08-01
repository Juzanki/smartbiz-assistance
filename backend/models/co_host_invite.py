from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class CoHostInvite(Base):
    __tablename__ = "co_host_invites"

    id = Column(Integer, primary_key=True, index=True)
    live_stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    host_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    invitee_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, default="pending")
    sent_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    stream = relationship("LiveStream", back_populates="cohost_invites")
    host = relationship("User", foreign_keys=[host_id])
    invitee = relationship("User", foreign_keys=[invitee_id])
