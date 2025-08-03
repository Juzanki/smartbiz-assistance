from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models.user import User
from backend.schemas.push_subscription import PushSubscriptionCreate, PushSubscriptionOut
from backend.crud import push_crud

router = APIRouter(
    prefix="/push",
    tags=["Push Notifications"]
)

@router.post("/subscribe", response_model=PushSubscriptionOut)
def subscribe_push(
    subscription: PushSubscriptionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if subscription.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return push_crud.create_or_update_subscription(db, subscription)
