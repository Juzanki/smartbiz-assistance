from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from backend.db import Base

class LiveSession(Base):
    """
    LiveSession model — represents a livestreaming session hosted by a user.
    Stores metadata like category, selected product IDs, and live status.
    """
    __tablename__ = "live_sessions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    category = Column(String(50), nullable=True)
    selected_products = Column(ARRAY(Integer))  # Only works with PostgreSQL
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)

    # Define the relationship to User
    user = relationship("User", back_populates="live_sessions")

    def __repr__(self):
        return f"<LiveSession(title='{self.title}', user_id={self.user_id}, active={self.active})>"
