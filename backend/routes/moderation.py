from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models.moderation import ModerationAction
from backend.schemas.moderation_schema import ModerationActionCreate, ModerationActionOut

router = APIRouter(prefix="/moderation", tags=["Moderation"])

@router.post("/", response_model=ModerationActionOut)
def apply_action(data: ModerationActionCreate, db: Session = Depends(get_db)):
    action = ModerationAction(**data.dict())
    db.add(action)
    db.commit()
    db.refresh(action)
    return action

@router.get("/{room_id}", response_model=List[ModerationActionOut])
def get_moderation_history(room_id: str, db: Session = Depends(get_db)):
    return db.query(ModerationAction).filter(ModerationAction.room_id == room_id).all()
