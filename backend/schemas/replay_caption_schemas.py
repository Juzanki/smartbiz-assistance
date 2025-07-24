from pydantic import BaseModel
from datetime import datetime

class ReplayCaptionCreate(BaseModel):
    stream_id: int
    text: str
    timestamp: datetime

class ReplayCaptionOut(BaseModel):
    id: int
    stream_id: int
    text: str
    timestamp: datetime

    class Config:
        orm_mode = True
