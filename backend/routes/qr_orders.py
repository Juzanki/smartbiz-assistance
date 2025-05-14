from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import Product
from backend.utils.qr_generator import generate_product_qr  # Base64 helper
from io import BytesIO
import qrcode
import os

router = APIRouter(prefix="/qr", tags=["QR Codes"])


# ========== 1. Generate QR for Product and Save Path ==========
@router.post("/products/{product_id}/generate", summary="🔲 Generate and store QR code for a product")
def create_product_qr(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    qr_url = f"https://smartbiz.com/order/{product_id}"

    try:
        # Generate QR image and save as file
        qr = qrcode.make(qr_url)
        qr_folder = "static/qr_codes"
        os.makedirs(qr_folder, exist_ok=True)

        file_path = os.path.join(qr_folder, f"product_{product_id}.png")
        qr.save(file_path)

        # Optionally save path in DB
        product.qr_code_url = file_path
        db.commit()

        return {
            "product_id": product_id,
            "qr_code_path": file_path,
            "link": qr_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR generation failed: {str(e)}")


# ========== 2. Generate Base64 QR for Any Data ==========
@router.get("/generate", summary="📦 Generate Base64 QR Code for a Product Link or Text")
def get_qr_base64(data: str = Query(..., min_length=3, description="Product link or any string")):
    """
    Generate a base64 QR image that can be embedded directly in frontend.
    """
    try:
        base64_qr = generate_product_qr(data)
        return {
            "input": data,
            "qr_code_base64": base64_qr,
            "preview": f"data:image/png;base64,{base64_qr}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR generation failed: {str(e)}")
