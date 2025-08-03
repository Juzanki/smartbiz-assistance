from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models.products_live import LiveProduct
from backend.schemas.products_live_schema import LiveProductCreate, LiveProductOut

router = APIRouter(prefix="/products-live", tags=["Live Products"])

@router.post("/", response_model=LiveProductOut)
def add_product_to_live(data: LiveProductCreate, db: Session = Depends(get_db)):
    live_product = LiveProduct(**data.dict())
    db.add(live_product)
    db.commit()
    db.refresh(live_product)
    return live_product

@router.get("/{room_id}", response_model=List[LiveProductOut])
def get_live_products(room_id: str, db: Session = Depends(get_db)):
    return db.query(LiveProduct).filter(LiveProduct.room_id == room_id).all()

@router.delete("/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    live_product = db.query(LiveProduct).filter(LiveProduct.product_id == product_id).first()
    if not live_product:
        raise HTTPException(status_code=404, detail="Product not found in live stream")
    db.delete(live_product)
    db.commit()
    return {"detail": "Product removed"}
