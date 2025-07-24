from pydantic import BaseModel

class ReplayEventCreate(BaseModel):
    stream_id: int
    content: str
    timestamp: str
