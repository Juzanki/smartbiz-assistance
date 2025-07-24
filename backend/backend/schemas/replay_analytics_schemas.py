from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReplayAnalyticsCreate(BaseModel):
    stream_id: int
    analysis_type: str
    result: str

class ReplayAnalyticsUpdate(BaseModel):
    analysis_type: Optional[str] = None
    result: Optional[str] = None

class ReplayAnalyticsOut(BaseModel):
    id: int
    stream_id: int
    analysis_type: str
    result: str
    created_at: datetime
