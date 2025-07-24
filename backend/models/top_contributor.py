from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from backend.db import Base

class TopContributor(Base):
    __tablename__ = "top_contributors"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("live_streams.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_value = Column(Integer, default=0)
    last_updated = Column(DateTime, default=datetime.utcnow)
