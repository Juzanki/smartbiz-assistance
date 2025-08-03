from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db import Base

class Guest(Base):
    """
    Represents a guest attempting or approved to join a live stream room.
    """
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(String, nullable=False, index=True, comment="Unique ID of the stream room")
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, comment="FK to User")
    is_approved = Column(Boolean, default=False, comment="True if approved by host")
    is_host = Column(Boolean, default=False, comment="True if this guest is the host")
    joined_at = Column(DateTime, default=datetime.utcnow, comment="Timestamp when guest joined")

    # Relationship to User model
    user = relationship("User", backref="guest_entries")
