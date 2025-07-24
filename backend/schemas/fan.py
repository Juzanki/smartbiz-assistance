from pydantic import BaseModel
from datetime import datetime

class FanCreate(BaseModel):
    user_id: int
    host_id: int
    total_contribution: float

class FanOut(BaseModel):
    id: int
    user_id: int
    host_id: int
    total_contribution: float
    last_contributed_at: datetime
