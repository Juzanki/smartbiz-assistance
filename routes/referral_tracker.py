from fastapi import APIRouter, Request, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import User
from fastapi.responses import JSONResponse, RedirectResponse
from datetime import timedelta

router = APIRouter(prefix="/referral", tags=["Referral Tracker"])


@router.get("/{username}", summary="📨 Track referral by username")
def track_referral(
    username: str,
    response: Response,
    db: Session = Depends(get_db)
):
    """
    Saves referral info via HTTP-only cookie.
    Triggered when someone visits /referral/{username}.
    """

    ref_user = db.query(User).filter(User.username == username).first()
    if not ref_user:
        raise HTTPException(status_code=404, detail="Invalid referral username.")

    # Set cookie valid for 7 days
    response = RedirectResponse(url="/", status_code=302)  # You can change this to your landing page
    response.set_cookie(
        key="ref_by",
        value=username,
        max_age=60 * 60 * 24 * 7,
        httponly=True,
        samesite="lax"
    )

    return response
