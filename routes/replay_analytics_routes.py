from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.replay_analytics import ReplayAnalytics
from backend.schemas.replay_analytics_schemas import ReplayAnalyticsUpdate
from sqlalchemy.exc import NoResultFound
from datetime import datetime

router = APIRouter()

@router.post("/increment")
def increment_field(data: ReplayAnalyticsUpdate, db: Session = Depends(get_db)):
    analytics = db.query(ReplayAnalytics).filter(ReplayAnalytics.stream_id == data.stream_id).first()
    if not analytics:
        analytics = ReplayAnalytics(stream_id=data.stream_id)
        db.add(analytics)
        db.commit()
        db.refresh(analytics)
    
    if data.field == "views":
        analytics.views += 1
    elif data.field == "likes":
        analytics.likes += 1
    elif data.field == "comments":
        analytics.comments += 1
    elif data.field == "shares":
        analytics.shares += 1
    elif data.field == "downloads":
        analytics.downloads += 1
    else:
        return {"error": "Unknown field"}

    db.commit()
    return {"message": f"{data.field} incremented", "analytics": {
        "views": analytics.views,
        "likes": analytics.likes,
        "comments": analytics.comments,
        "shares": analytics.shares,
        "downloads": analytics.downloads
    }}
