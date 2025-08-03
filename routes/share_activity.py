from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models.share_activity import ShareActivity
from backend.schemas.share_activity_schema import ShareActivityCreate, ShareActivityOut

router = APIRouter(prefix="/share-activity", tags=["Share Activity"])

@router.post("/", response_model=ShareActivityOut)
def log_share(data: ShareActivityCreate, db: Session = Depends(get_db)):
    record = ShareActivity(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/by-room/{room_id}", response_model=List[ShareActivityOut])
def get_room_shares(room_id: str, db: Session = Depends(get_db)):
    return db.query(ShareActivity).filter(ShareActivity.room_id == room_id).all()

@router.get("/by-user/{user_id}", response_model=List[ShareActivityOut])
def get_user_shares(user_id: int, db: Session = Depends(get_db)):
    return db.query(ShareActivity).filter(ShareActivity.user_id == user_id).all()
