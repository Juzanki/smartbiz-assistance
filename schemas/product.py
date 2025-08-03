from datetime import datetime
from pydantic import BaseModel

# --- ProductOut ---


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True
