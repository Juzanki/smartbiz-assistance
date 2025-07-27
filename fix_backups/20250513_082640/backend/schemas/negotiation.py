from typing import Optional
from pydantic import BaseModel

# --- NegotiationRequest ---
class NegotiationRequest(BaseModel):
    product_id: int
    user_message: str

# --- NegotiationResponse ---
class NegotiationResponse(BaseModel):
    product_name: str
    original_price: float
    proposed_reply: str
    suggested_discount: Optional[float] = None
