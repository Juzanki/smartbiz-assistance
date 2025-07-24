from pydantic import BaseModel

class CaptionRequest(BaseModel):
    video_url: str
    timestamp: str  # HH:MM:SS
