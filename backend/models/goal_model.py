from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from backend.db import Base
from datetime import datetime

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    goal_type = Column(String(50), nullable=False)  # e.g. "likes", "coins", "gifts"
    title = Column(String(100), nullable=False)
    target_value = Column(Float, nullable=False)
    current_value = Column(Float, default=0.0)
    expires_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
