from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models import Product
from backend.auth import get_current_user
from backend.schemas import ProductOut

router = APIRouter(prefix="/products", tags=["Product Search"])


@router.get("/search", response_model=List[ProductOut], summary="🔍 Auto Search Products")
def search_products(
    query: str = Query(..., min_length=2, description="Search keyword"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Search for products based on partial match in product name.
    Requires authentication.
    """
    results = db.query(Product).filter(Product.name.ilike(f"%{query}%")).limit(20).all()
    return results
