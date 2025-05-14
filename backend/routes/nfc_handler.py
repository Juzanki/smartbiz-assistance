from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/nfc", tags=["NFC"])


# ========== Response Schema ==========
class NFCScanResponse(BaseModel):
    message: str
    nfc_id: str
    next_step: str


# ========== Endpoint ==========
@router.get("/{nfc_id}", response_model=NFCScanResponse, summary="📶 Handle NFC tag scan")
def read_nfc(nfc_id: str):
    """
    Simulates NFC tag scan.
    Future versions will map the tag to a product, order, or asset.
    """
    return NFCScanResponse(
        message="🧪 NFC feature in preview mode",
        nfc_id=nfc_id,
        next_step="✅ Scan successful, show product or asset details"
    )
