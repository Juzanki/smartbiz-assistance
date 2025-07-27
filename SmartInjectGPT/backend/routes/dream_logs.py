from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import SessionLocal, get_db
from backend.schemas.dream_log import DreamLogCreate, DreamLogOut
from backend.crud import dream_log

router = APIRouter()

@router.post("/api/logs", response_model=DreamLogOut)
def log_prompt(data: DreamLogCreate, db: Session = Depends(get_db)):
    return dream_log.create_dream_log(db, data)

@router.get("/api/logs", response_model=list[DreamLogOut])
def list_logs(db: Session = Depends(get_db)):
    return dream_log.get_all_logs(db)
