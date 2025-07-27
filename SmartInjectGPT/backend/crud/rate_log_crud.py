from sqlalchemy.orm import Session
from backend.models.rate_log import APIRateLog
from backend.schemas.rate_log import APIRateLogCreate

def create_rate_log(db: Session, log_data: APIRateLogCreate):
    log = APIRateLog(**log_data.dict())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
