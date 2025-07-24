from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.gift import GiftCreate, GiftOut
from backend.crud import gift_crud
from backend.db import get_db

router = APIRouter(prefix="/gifts", tags=["Gifts"])

@router.post("/", response_model=GiftOut)
def create_gift(gift: GiftCreate, db: Session = Depends(get_db)):
    existing = gift_crud.get_gift_by_name(db, gift.name)
    if existing:
        raise HTTPException(status_code=400, detail="Gift with that name already exists.")
    return gift_crud.create_gift(db, gift)

@router.get("/", response_model=list[GiftOut])
def list_gifts(db: Session = Depends(get_db)):
    return gift_crud.get_all_gifts(db)
