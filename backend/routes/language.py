from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models import User
from backend.schemas import LanguagePreferenceUpdate

router = APIRouter(prefix="/profile", tags=["Language Settings"])


@router.put("/language", summary="🌍 Update language preference")
def update_language(
    payload: LanguagePreferenceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Updates the preferred language of the currently authenticated user.
    Example: `sw` for Kiswahili, `en` for English, etc.
    """

    supported_languages = ["en", "sw", "fr", "es", "ar", "zh", "hi", "pt", "ru", "de", "ja", "tr"]

    if payload.language not in supported_languages:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported language: {payload.language}"
        )

    current_user.language = payload.language
    db.commit()
    db.refresh(current_user)

    return {
        "message": f"✅ Language preference updated to '{payload.language}'",
        "user_id": current_user.id,
        "new_language": current_user.language
    }
