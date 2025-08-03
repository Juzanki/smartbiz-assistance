from pydantic import BaseModel
from datetime import datetime

class TopContributorUpdate(BaseModel):
    stream_id: int
    user_id: int
    value: int

class TopContributorOut(BaseModel):
    user_id: int
    total_value: int
    last_updated: datetime
