from typing import List
from pydantic import BaseModel

# --- BroadcastMessage ---
class BroadcastMessage(BaseModel):
    message: str
    channels: List[str]
