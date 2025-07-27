# backend/models/ai_module.py

from sqlalchemy import Column, Integer, String
from backend.db import Base

class AIModule(Base):
    __tablename__ = "ai_modules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    version = Column(String, nullable=True)

    def __repr__(self):
        return f"<AIModule(id={self.id}, name='{self.name}', version='{self.version}')>"
