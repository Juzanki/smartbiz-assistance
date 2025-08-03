from sqlalchemy import Column, Integer, String, Boolean, DateTime
from backend.db import Base
from datetime import datetime

class Filter(Base):
    __tablename__ = "filters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(100), unique=True, nullable=False)  # e.g., "neon", "glow"
    css_class = Column(String(255), nullable=False)          # e.g., "filter-neon"
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
