from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from backend.db import get_db
from backend.models import Order, Product, ReferralLog, User
from backend.dependencies import get_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])


# ========== Request Schema ==========
class CheckoutRequest(BaseModel):
    product_id: int


# ========== Endpoint ==========
@router.post("/checkout", summary="🛒 Create Order + Handle Referral")
def create_order(
    payload: CheckoutRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    ref_by: str = Cookie(default=None)  # read from cookie, not session
):
    # Check if product exists
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Create new order
    order = Order(
        user_id=current_user.id,
        product_id=product.id,
        price=product.price,
        created_at=datetime.utcnow()
    )
    db.add(order)

    # Optional: handle referral commission
    if ref_by:
        ref_user = db.query(User).filter(User.username == ref_by).first()
        if ref_user and ref_user.id != current_user.id:
            commission = round(product.price * 0.10, 2)
            referral = ReferralLog(
                promoter_id=ref_user.id,
                product_name=product.name,
                buyer_name=current_user.username,
                amount=commission,
                status="pending",
                created_at=datetime.utcnow()
            )
            db.add(referral)

    db.commit()

    return {
        "message": "✅ Order created successfully.",
        "product": {
            "id": product.id,
            "name": product.name,
            "price": product.price
        },
        "buyer": current_user.email,
        "referral_tracked": bool(ref_by)
    }
