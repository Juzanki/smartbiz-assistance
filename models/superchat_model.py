from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from backend.db import Base
from datetime import datetime

class Superchat(Base):
    __tablename__ = "superchats"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, nullable=False)
    stream_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    message = Column(String(300))
    emoji = Column(String(20))
    animation_id = Column(String(100))
    voice_clip_url = Column(String(255))
    highlight_color = Column(String(20), default="#FFD700")  # Default to gold
    timestamp = Column(DateTime, default=datetime.utcnow)
