from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GoalCreate(BaseModel):
    creator_id: int
    goal_type: str
    title: str
    target_value: float
    expires_at: Optional[datetime] = None

class GoalOut(BaseModel):
    id: int
    creator_id: int
    goal_type: str
    title: str
    target_value: float
    current_value: float
    expires_at: Optional[datetime]
    created_at: datetime
