from datetime import datetime
from pydantic import BaseModel

# --- WebhookEndpoint ---

class WebhookEndpointBase(BaseModel):
    url: str
    secret: str | None = None
    is_active: bool = True

class WebhookEndpointCreate(WebhookEndpointBase):
    user_id: int

class WebhookEndpointOut(WebhookEndpointBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- WebhookDeliveryLog ---

class WebhookDeliveryLogOut(BaseModel):
    id: int
    endpoint_id: int
    payload: str
    response_code: int | None
    success: bool
    attempts: int
    error_message: str | None
    delivered_at: datetime

    class Config:
        from_attributes = True
