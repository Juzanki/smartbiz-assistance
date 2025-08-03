from sqlalchemy import Column, Integer, String, DateTime, func
from backend.db import Base

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(String, index=True)
    user_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
