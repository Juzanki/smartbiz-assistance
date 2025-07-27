from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

from backend.db import get_db
from backend.models.rate_log import APIRateLog
from backend.schemas.rate_log import APIRateLogCreate
from backend.schemas.api_key import APIKeyOut  # just in case needed
from backend.dependencies import get_current_admin  # admin auth

router = APIRouter(prefix="/admin", tags=["Admin Logs"])

@router.get("/api-logs", response_model=List[APIRateLogCreate])
def get_api_usage_logs(
    db: Session = Depends(get_db),
    api_key_id: Optional[int] = Query(None),
    method: Optional[str] = Query(None),
    endpoint: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    _: dict = Depends(get_current_admin)  # Only admin allowed
):
    query = db.query(APIRateLog)

    if api_key_id:
        query = query.filter(APIRateLog.api_key_id == api_key_id)
    if method:
        query = query.filter(APIRateLog.method.ilike(method))
    if endpoint:
        query = query.filter(APIRateLog.endpoint.ilike(f"%{endpoint}%"))
    if start_date:
        query = query.filter(APIRateLog.timestamp >= start_date)
    if end_date:
        query = query.filter(APIRateLog.timestamp <= end_date)

    return query.order_by(APIRateLog.timestamp.desc()).all()
