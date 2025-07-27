from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from backend.db import Base

class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True, nullable=False)
    plan = Column(String, default="free")
    owner_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
