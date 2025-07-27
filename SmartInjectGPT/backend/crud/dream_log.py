from sqlalchemy.orm import Session
from backend.models.dream_log import DreamLog
from backend.schemas.dream_log import DreamLogCreate

def create_dream_log(db: Session, data: DreamLogCreate) -> DreamLog:
    log = DreamLog(prompt=data.prompt)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_all_logs(db: Session):
    return db.query(DreamLog).order_by(DreamLog.created_at.desc()).all()
