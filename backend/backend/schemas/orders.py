from datetime import datetime
from pydantic import BaseModel

# --- SmartOrderOut ---


class SmartOrderOut(BaseModel):
    id: int
    customer_name: str
    product_id: int
    method: str
    created_at: datetime
    status: str

    class Config:
        from_attributes = True
