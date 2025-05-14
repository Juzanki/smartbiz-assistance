from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import LiveSession, Product
from typing import List

router = APIRouter(prefix="/live", tags=["Live"])


@router.get("/current", summary="🎥 Get Current Active Live Session")
def get_current_live(
    db: Session = Depends(get_db),
):
    """
    Returns the current active live session with floating products (if any).
    """
    live = db.query(LiveSession).filter(LiveSession.active.is_(True))\
        .order_by(LiveSession.started_at.desc()).first()

    if not live:
        raise HTTPException(
            status_code=404, detail="No active live session found."
        )

    product_data = []
    if live.selected_products:
        product_data = db.query(Product).filter(
            Product.id.in_(live.selected_products)
        ).all()

    return {
        "live": {
            "id": live.id,
            "title": live.title,
            "category": live.category,
            "started_at": live.started_at,
            "user_id": live.user_id
        },
        "products": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "image": p.image_url
            } for p in product_data
        ]
    }
