from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models.live_stream import LiveStream
from backend.schemas.explore_schema import LiveStreamExploreOut

router = APIRouter(prefix="/explore", tags=["Explore"])

@router.get("/featured", response_model=List[LiveStreamExploreOut])
def get_featured_streams(db: Session = Depends(get_db)):
    return db.query(LiveStream).filter(
        LiveStream.is_featured == True,
        LiveStream.is_live == True
    ).order_by(LiveStream.started_at.desc()).all()

@router.get("/trending", response_model=List[LiveStreamExploreOut])
def get_trending_streams(db: Session = Depends(get_db)):
    return db.query(LiveStream).filter(
        LiveStream.is_live == True
    ).order_by(LiveStream.viewers_count.desc(), LiveStream.gifts_count.desc()).limit(20).all()
