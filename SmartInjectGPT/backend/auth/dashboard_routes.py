from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user

router = APIRouter()

@router.get("/dashboard", tags=["Protected"])
def get_dashboard(current_user: str = Depends(get_current_user)):
    return {"message": f"✅ Welcome to your dashboard, {current_user}!"}
