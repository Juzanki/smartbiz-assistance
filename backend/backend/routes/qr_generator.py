from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import qrcode
import base64
from io import BytesIO

router = APIRouter(prefix="/qr", tags=["QR Codes"])


# ========== Route: Return PNG Image ==========
@router.get("/generate-image/{product_id}", summary="📷 Generate PNG QR for a product")
def generate_qr_image(product_id: int):
    """
    Generates a downloadable PNG QR code that links to a product page.
    Suitable for embedding in marketing materials or labels.
    """
    try:
        url = f"https://smartbiz.com/product/{product_id}"
        qr = qrcode.make(url)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        buf.seek(0)
        return StreamingResponse(buf, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"QR generation failed: {str(e)}")


# ========== Helper: Return Base64 QR ==========
def generate_product_qr(data: str) -> str:
    """
    Generates a base64-encoded QR code image from a given URL or string.
    Can be used for inline image display in frontend or JSON.
    """
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    except Exception as e:
        raise Exception(f"QR Base64 generation failed: {str(e)}")
