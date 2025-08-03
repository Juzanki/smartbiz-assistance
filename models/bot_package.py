# backend/models/bot_package.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from backend.db import Base
from sqlalchemy.orm import relationship

class BotPackage(Base):
    __tablename__ = "bot_packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    price_monthly = Column(Float, default=0.0)
    price_yearly = Column(Float, default=0.0)
    features = Column(String)  # JSON stringified array
    created_at = Column(DateTime, default=datetime.utcnow)

    # ? Sahihi relationship
    bots = relationship("UserBot", back_populates="package", cascade="all, delete-orphan")
