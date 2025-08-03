from pydantic import BaseModel
from datetime import datetime

class RecordedStreamCreate(BaseModel):
    stream_id: int
    file_path: str
    duration: float

class RecordedStreamOut(BaseModel):
    id: int
    stream_id: int
    file_path: str
    duration: float
    uploaded_at: datetime

    class Config:
        from_attributes = True
