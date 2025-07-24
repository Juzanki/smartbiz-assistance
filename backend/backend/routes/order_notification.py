# backend/routes/order_notification.py

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/orders", tags=["Order Notifications"])


# ========== Response Schema ==========
class OrderStatusResponse(BaseModel):
    status: str
    timestamp: str


# ========== Endpoint ==========
@router.get("/status", response_model=OrderStatusResponse, summary="📦 Check current order status")
def order_status():
    """
    Returns the current status of a user's order.
    In future: status may include steps like confirmed, packed, shipped, delivered.
    """
    return OrderStatusResponse(
        status="🛒 Order is being processed",
        timestamp=datetime.utcnow().isoformat()
    )
