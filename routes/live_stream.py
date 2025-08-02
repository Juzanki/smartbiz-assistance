from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import LiveSession, Product
from backend.schemas.live_stream_schema import LiveStreamOut
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

from sqlalchemy.sql import func

@router.post("/end/{stream_id}", response_model=LiveStreamOut)
def end_live_stream(stream_id: int, db: Session = Depends(get_db)):
    stream = db.query(LiveStream).filter(LiveStream.id == stream_id).first()
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")

    if stream.ended_at:
        raise HTTPException(status_code=400, detail="Stream already ended")

    stream.ended_at = func.now()
    db.commit()
    db.refresh(stream)
    return stream
