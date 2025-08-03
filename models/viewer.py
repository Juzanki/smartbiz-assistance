from sqlalchemy import Column, Integer, String, DateTime
from backend.db import Base
from datetime import datetime

class Viewer(Base):
    __tablename__ = "viewers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    stream_id = Column(String, nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
