from pydantic import BaseModel
from datetime import datetime

class ReplayHighlightCreate(BaseModel):
    title: str
    timestamp: str

class ReplayHighlightOut(BaseModel):
    id: int
    title: str
    timestamp: str
    created_at: datetime

    class Config:
        from_attributes = True
