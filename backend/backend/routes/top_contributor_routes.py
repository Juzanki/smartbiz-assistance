from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.top_contributor import TopContributor
from backend.schemas.top_contributor_schemas import TopContributorUpdate
from datetime import datetime

router = APIRouter()

@router.post("/update")
def update_top_contributor(data: TopContributorUpdate, db: Session = Depends(get_db)):
    record = db.query(TopContributor).filter_by(stream_id=data.stream_id, user_id=data.user_id).first()
    if record:
        record.total_value += data.value
        record.last_updated = datetime.utcnow()
    else:
        record = TopContributor(
            stream_id=data.stream_id,
            user_id=data.user_id,
            total_value=data.value,
            last_updated=datetime.utcnow()
        )
        db.add(record)
    db.commit()
    return {"message": "Contributor updated", "user_id": data.user_id}

@router.get("/stream/{stream_id}")
def get_top_contributors(stream_id: int, db: Session = Depends(get_db)):
    contributors = db.query(TopContributor).filter_by(stream_id=stream_id).order_by(TopContributor.total_value.desc()).limit(10).all()
    return contributors
