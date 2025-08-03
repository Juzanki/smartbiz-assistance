from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from backend.db import get_db
from backend.models import Campaign, Product, User
from backend.schemas import CampaignCreate, CampaignOut
from backend.dependencies import get_current_user

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])

# 📢 Create a new marketing campaign
@router.post("/create", summary="📢 Create a new marketing campaign")
def create_campaign(
    payload: CampaignCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()

    if not product or product.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid product or permission denied"
        )

    ends_at = datetime.utcnow() + timedelta(days=payload.duration)

    campaign = Campaign(
        title=payload.title,
        product_id=payload.product_id,
        owner_id=current_user.id,
        commission_rate=payload.rate,
        ends_at=ends_at
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    return {
        "message": "✅ Campaign created successfully",
        "campaign_id": campaign.id
    }

# 🔍 View campaigns created by the current user
@router.get("/my", summary="🔍 View my campaigns", response_model=list[CampaignOut])
def get_my_campaigns(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    campaigns = db.query(Campaign).filter(Campaign.owner_id == current_user.id).all()
    return campaigns
