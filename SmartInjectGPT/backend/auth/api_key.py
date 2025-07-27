# backend/auth/api_key.py

from fastapi import Header, HTTPException, status
import os
import logging

async def verify_admin_key(x_admin_key: str = Header(...)):
    """
    ✅ Verify incoming X-Admin-Key against SMARTINJECT_SECRET from environment.
    Only trusted systems (like SmartBiz Assistance) should have the correct key.
    """
    expected_key = os.getenv("SMARTINJECT_SECRET")

    if not expected_key:
        logging.error("❌ SMARTINJECT_SECRET is not configured in environment.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server misconfiguration: Admin secret is missing"
        )

    if x_admin_key != expected_key:
        logging.warning("⚠️ Unauthorized access attempt to SmartInjectGPT detected.")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="❌ Unauthorized: Invalid admin key"
        )

    logging.info("🔐 Admin key verified successfully.")
