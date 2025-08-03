from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.replay_caption import ReplayCaption
from backend.schemas.replay_caption_schemas import ReplayCaptionCreate, ReplayCaptionOut

router = APIRouter()

@router.post("/", response_model=ReplayCaptionOut)
def add_caption(data: ReplayCaptionCreate, db: Session = Depends(get_db)):
    caption = ReplayCaption(**data.dict())
    db.add(caption)
    db.commit()
    db.refresh(caption)
    return caption

@router.get("/{stream_id}", response_model=list[ReplayCaptionOut])
def get_captions(stream_id: int, db: Session = Depends(get_db)):
    return db.query(ReplayCaption).filter_by(stream_id=stream_id).all()
