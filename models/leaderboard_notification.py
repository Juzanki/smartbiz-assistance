from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from datetime import datetime
from backend.db import Base

class LeaderboardNotification(Base):
    __tablename__ = "leaderboard_notifications"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    position = Column(Integer, nullable=False)
    previous_position = Column(Integer, nullable=True)
    type = Column(String)  # 'rise', 'drop', 'new'
    seen = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
