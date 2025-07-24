from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class ActionType(str, Enum):
    mute = "mute"
    block = "block"
    report = "report"

class ModerationActionCreate(BaseModel):
    room_id: str
    target_user_id: int
    moderator_id: int
    action: ActionType
    reason: str = None

class ModerationActionOut(BaseModel):
    id: int
    room_id: str
    target_user_id: int
    moderator_id: int
    action: ActionType
    reason: str = None
    timestamp: datetime
