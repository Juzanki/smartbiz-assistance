# backend/routes/qr_code.py

from fastapi import APIRouter, HTTPException, Query
from backend.utils.qr_generator import generate_product_qr
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/qr", tags=["QR Codes"])


# ========== Response Schema ==========
class QRCodeResponse(BaseModel):
    product_id: int
    qr_code_base64: str
    link: str


# ========== Endpoint ==========
@router.get("/product", response_model=QRCodeResponse, summary="📦 Generate product QR code")
def get_qr_code(product_id: int = Query(..., gt=0, description="Unique product ID")):
    """
    Generates and returns a base64 QR code image that links to a public product page.
    Example usage: marketing flyers, offline store displays, etc.
    """
    product_url = f"https://smartbiz.com/products/{product_id}"
    try:
        qr_base64 = generate_product_qr(product_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate QR: {str(e)}")

    return QRCodeResponse(
        product_id=product_id,
        qr_code_base64=qr_base64,
        link=product_url
    )
