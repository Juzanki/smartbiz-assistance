from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from backend.db import get_db
from backend.auth import get_current_user
from backend.models import User

router = APIRouter(prefix="/subscription", tags=["Subscription Plans"])


# ==================== SCHEMAS ====================
class SubscriptionPlan(BaseModel):
    id: int
    name: str
    price: int
    duration_days: int
    features: str


class PurchaseRequest(BaseModel):
    plan_name: str


class PurchaseResponse(BaseModel):
    message: str
    plan: str
    expires: str


# ==================== STATIC PLAN DATA ====================
PLANS = [
    SubscriptionPlan(
        id=1,
        name="Pro",
        price=30000,
        duration_days=30,
        features="Access to AI Bot, Smart Scheduling, Premium Support"
    ),
    SubscriptionPlan(
        id=2,
        name="Business",
        price=65000,
        duration_days=30,
        features="Everything in Pro + Team Access + Insights"
    ),
    SubscriptionPlan(
        id=3,
        name="Enterprise",
        price=125000,
        duration_days=30,
        features="Unlimited Access, White-labeling, Enterprise Integrations"
    )
]

# ✅ Dictionary for lookup (lowercase keys for flexibility)
plans_dict = {plan.name.lower(): plan for plan in PLANS}


# ==================== ROUTES ====================
@router.get("/plans", response_model=list[SubscriptionPlan], summary="📦 View all subscription plans")
def get_subscription_plans():
    return PLANS


@router.post("/purchase", response_model=PurchaseResponse, status_code=status.HTTP_200_OK, summary="💳 Subscribe to a plan")
def purchase_plan(
    purchase: PurchaseRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    plan = plans_dict.get(purchase.plan_name.lower())
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    persistent_user = db.merge(current_user)

    # Optional: Avoid double-purchase
    if persistent_user.subscription_status.lower() == plan.name.lower():
        raise HTTPException(status_code=400, detail=f"Already subscribed to {plan.name}")

    # Update subscription
    persistent_user.subscription_status = plan.name
    persistent_user.subscription_expiry = datetime.utcnow() + timedelta(days=plan.duration_days)

    db.commit()
    db.refresh(persistent_user)

    return PurchaseResponse(
        message="✅ Subscription successful",
        plan=plan.name,
        expires=persistent_user.subscription_expiry.strftime("%Y-%m-%d %H:%M:%S")
    )
