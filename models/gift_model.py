from sqlalchemy import Column, Integer, String
from backend.db import Base
from sqlalchemy.orm import relationship

class Gift(Base):
    __tablename__ = "gifts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    coins = Column(Integer, nullable=False)
    tier = Column(String, nullable=False)  # e.g., "Rare"
    icon_path = Column(String, nullable=False)
    animation_path = Column(String, nullable=True)
    description = Column(String, nullable=True)
    movements = relationship("GiftMovement", back_populates="gift", cascade="all, delete-orphan")
