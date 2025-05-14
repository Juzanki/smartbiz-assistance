"""
Model: APIKey
Purpose: Stores generated API keys for system integrations.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from backend.db import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    key = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<APIKey(name='{self.name}', key='{self.key[:6]}...')>"
