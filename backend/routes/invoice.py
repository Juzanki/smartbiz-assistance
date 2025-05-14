from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from backend.services.pdf_service import send_invoice

router = APIRouter(prefix="/invoice", tags=["Invoices"])


# ========== Schema ==========
class InvoiceData(BaseModel):
    name: str = Field(..., example="Julius Zakayo")
    amount: str = Field(..., example="15000")
    description: str = Field(..., example="Business Support Plan")


class InvoiceRequest(BaseModel):
    template: dict = Field(..., example={"id": "your_template_id"})
    data: InvoiceData


# ========== Endpoint ==========
@router.post("/generate", summary="🧾 Generate and Send Invoice")
def generate_invoice(payload: InvoiceRequest):
    """
    Generates an invoice using provided template ID and data.
    Calls an internal PDF service.
    """
    try:
        result = send_invoice(payload.dict())
        return {"status": "✅ success", "invoice": result}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"❌ Failed to generate invoice: {str(e)}"
        )
