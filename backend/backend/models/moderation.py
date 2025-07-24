from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from backend.db import Base
import enum

class ActionType(str, enum.Enum):
    mute = "mute"
    block = "block"
    report = "report"

class ModerationAction(Base):
    __tablename__ = "moderation_actions"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(String, index=True)
    target_user_id = Column(Integer)
    moderator_id = Column(Integer)
    action = Column(Enum(ActionType))
    reason = Column(String, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
