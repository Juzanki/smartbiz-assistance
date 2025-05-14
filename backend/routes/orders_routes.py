from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import Product

router = APIRouter()


@router.get("/nfc/product-info", summary="Fetch product by NFC tag")
def get_product_by_nfc(
    tag_id: str = Query(..., description="Unique NFC tag ID"),
    db: Session = Depends(get_db)
):
    """
    Retrieve product info linked to a given NFC tag ID.
    """
    product = db.query(Product).filter(Product.nfc_tag == tag_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return {
        "product_id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    }