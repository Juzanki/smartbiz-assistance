from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# --- PaymentRequest ---
class PaymentRequest(BaseModel):
    amount: float
    phone_number: str
    reference: Optional[str] = None

# --- PaymentResponse ---
class PaymentResponse(BaseModel):
    id: str
    reference: str
    amount: float
    status: str
    phone_number: str
    method: str
    created_at: datetime
    instructions: str

# --- ConfirmMpesaRequest ---
class ConfirmMpesaRequest(BaseModel):
    reference: str
