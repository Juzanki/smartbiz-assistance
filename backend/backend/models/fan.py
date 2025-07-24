from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from backend.db import Base
from datetime import datetime

class Fan(Base):
    __tablename__ = "fans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    host_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_contribution = Column(Float, default=0.0)
    last_contributed_at = Column(DateTime, default=datetime.utcnow)
