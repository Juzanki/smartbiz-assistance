from pydantic import BaseModel
from datetime import datetime

# ✅ Schema ya kuunda ujumbe mpya (incoming request)
class ChatCreate(BaseModel):
    sender_id: int
    room_id: str
    message: str

# ✅ Schema ya kuonyesha ujumbe (outgoing response)
class ChatOut(BaseModel):
    id: int
    sender_id: int
    room_id: str
    message: str
    timestamp: datetime

    class Config:
        from_attributes = True  # 🔄 Badala ya orm_mode
