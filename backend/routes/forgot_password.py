"""
Forgot Password Flow for SmartBiz Assistant.
Handles sending, verifying, and resetting passwords using verification codes.
"""

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.models import PasswordResetCode
from backend.schemas import ForgotPasswordRequest, VerifyResetCode, ResetPassword
from backend.utils.verification import generate_verification_code
from backend.crud.user_crud import get_user_by_identifier
from backend.utils.security import get_password_hash

router = APIRouter(prefix="/auth/forgot-password", tags=["Password Reset"])

# ====================== Send Reset Code ======================

@router.post("", summary="📨 Send password reset code to user")
def send_reset_code(
    payload: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    """
    Generate and store a password reset code for a user using email or phone number.
    Sends the code via SMS or email (simulation only for now).
    """
    user = get_user_by_identifier(db, payload.identifier)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Optional: Delete existing codes for this identifier
    db.query(PasswordResetCode).filter_by(identifier=payload.identifier).delete()

    code = generate_verification_code()
    expires_at = datetime.utcnow() + timedelta(minutes=5)

    reset_entry = PasswordResetCode(
        identifier=payload.identifier,
        code=code,
        expires_at=expires_at
    )
    db.add(reset_entry)
    db.commit()

    # Replace this with actual email or SMS integration
    print(f"[DEBUG] Verification code sent to {payload.identifier}: {code}")

    return {"message": "✅ Verification code sent successfully"}

# ====================== Verify Reset Code ======================

@router.post("/verify-reset-code", summary="🔍 Verify the reset code")
def verify_code(
    payload: VerifyResetCode,
    db: Session = Depends(get_db)
):
    """
    Verify that the provided reset code matches and is not expired.
    """
    record = db.query(PasswordResetCode).filter_by(
        identifier=payload.identifier,
        code=payload.code
    ).first()

    if not record or record.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="❌ Invalid or expired verification code"
        )

    return {"message": "✅ Verification code is valid"}

# ====================== Reset Password ======================

@router.post("/reset-password", summary="🔒 Reset password after verification")
def reset_password(
    payload: ResetPassword,
    db: Session = Depends(get_db)
):
    """
    Reset the user's password if the verification code is valid and unexpired.
    """
    record = db.query(PasswordResetCode).filter_by(
        identifier=payload.identifier,
        code=payload.code
    ).first()

    if not record or record.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="❌ Invalid or expired verification code"
        )

    user = get_user_by_identifier(db, payload.identifier)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password = get_password_hash(payload.new_password)

    # Delete reset code after successful password update
    db.delete(record)
    db.commit()

    return {"message": "🔐 Password has been reset successfully"}
