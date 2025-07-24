from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.replay_analytics import ReplayAnalytics
from backend.schemas.replay_analytics_schemas import ReplayAnalyticsCreate, ReplayAnalyticsOut

router = APIRouter()

@router.post("/", response_model=ReplayAnalyticsOut)
def save_analytics(data: ReplayAnalyticsCreate, db: Session = Depends(get_db)):
    entry = ReplayAnalytics(**data.dict())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

@router.get("/{stream_id}", response_model=list[ReplayAnalyticsOut])
def get_analytics(stream_id: int, db: Session = Depends(get_db)):
    return db.query(ReplayAnalytics).filter_by(stream_id=stream_id).order_by(ReplayAnalytics.timestamp).all()
