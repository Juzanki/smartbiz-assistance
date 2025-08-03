"""
Handles Pesapal payment redirection and callback processing.
"""

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse
import os

router = APIRouter()

# Load credentials from environment
PESAPAL_CALLBACK_URL = os.getenv("PESAPAL_CALLBACK_URL")
PESAPAL_CONSUMER_KEY = os.getenv("PESAPAL_CONSUMER_KEY")
PESAPAL_CONSUMER_SECRET = os.getenv("PESAPAL_CONSUMER_SECRET")

@router.post("/pay/pesapal", summary="Start Pesapal Payment (Redirect)")
async def start_pesapal_payment(request: Request):
    # NOTE: Normally you'd generate a payment URL from Pesapal API
    fake_payment_url = "https://pay.pesapal.com/mock/redirect?reference=TX12345"
    return RedirectResponse(fake_payment_url)

@router.post("/wallet/pesapal/callback", status_code=200)
async def pesapal_callback_handler(request: Request):
    """Receive payment status from Pesapal callback (called via env PESAPAL_CALLBACK_URL)"""
    body = await request.body()
    print("📩 PESAPAL CALLBACK RECEIVED:", body.decode())
    return {"status": "callback_received"}
