# backend/routes/smart_orders.py

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from datetime import datetime

from backend.db import get_db
from backend.models import Order, Product, User
from backend.auth import get_current_user

router = APIRouter(prefix="/smart-orders", tags=["Smart Orders"])


# ====================== Schema ======================
class SmartOrderRequest(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")


class SmartOrderResponse(BaseModel):
    message: str
    order_id: int
    product: str
    quantity: int
    total: float


# ====================== Endpoint ======================
@router.post("/place", response_model=SmartOrderResponse, summary="🧾 Place order via QR/NFC scan")
def place_smart_order(
    order: SmartOrderRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == order.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.stock < order.quantity:
        raise HTTPException(status_code=400, detail="Insufficient stock available")

    total_price = order.quantity * product.price

    new_order = Order(
        user_id=current_user.id,
        product_id=product.id,
        quantity=order.quantity,
        total=total_price,
        status="pending",
        created_at=datetime.utcnow()
    )

    # Real-time stock update
    product.stock -= order.quantity

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return SmartOrderResponse(
        message="✅ Order placed successfully via QR/NFC",
        order_id=new_order.id,
        product=product.name,
        quantity=order.quantity,
        total=total_price
    )
