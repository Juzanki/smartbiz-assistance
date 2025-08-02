from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.fan import FanCreate, FanOut
from backend.crud import fan_crud
from backend.db import get_db

router = APIRouter(prefix="/fans", tags=["Fans"])

@router.post("/", response_model=FanOut)
def create_or_update_fan(fan: FanCreate, db: Session = Depends(get_db)):
    return fan_crud.create_or_update_fan(db, fan)

@router.get("/top/{host_id}", response_model=list[FanOut])
def get_top_fans(host_id: int, db: Session = Depends(get_db)):
    return fan_crud.get_top_fans(db, host_id)
