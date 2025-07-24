from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.replay_summary import ReplaySummary
from backend.schemas.replay_summary_schemas import ReplaySummaryCreate, ReplaySummaryOut

router = APIRouter()

@router.post("/", response_model=ReplaySummaryOut)
def save_summary(data: ReplaySummaryCreate, db: Session = Depends(get_db)):
    summary = ReplaySummary(**data.dict())
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary

@router.get("/{stream_id}", response_model=ReplaySummaryOut)
def get_summary(stream_id: int, db: Session = Depends(get_db)):
    return db.query(ReplaySummary).filter_by(stream_id=stream_id).first()
