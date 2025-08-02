from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.replay_title import ReplayTitle
from backend.schemas.replay_title_schemas import ReplayTitleCreate, ReplayTitleOut

router = APIRouter()

@router.post("/", response_model=ReplayTitleOut)
def save_title(data: ReplayTitleCreate, db: Session = Depends(get_db)):
    title = ReplayTitle(**data.dict())
    db.add(title)
    db.commit()
    db.refresh(title)
    return title

@router.get("/{stream_id}", response_model=ReplayTitleOut)
def get_title(stream_id: int, db: Session = Depends(get_db)):
    return db.query(ReplayTitle).filter_by(stream_id=stream_id).first()
