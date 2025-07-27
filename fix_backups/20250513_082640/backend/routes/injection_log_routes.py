from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.injection_log import InjectionLogOut
from backend.crud.injection_log import get_logs

router = APIRouter()

@router.get("/injection-logs", response_model=list[InjectionLogOut])
def read_logs(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return get_logs(db, skip=skip, limit=limit)
