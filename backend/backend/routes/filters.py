from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.filter import FilterCreate, FilterOut
from backend.crud import filter_crud

router = APIRouter()

@router.post("/", response_model=FilterOut)
def create_filter(filter_data: FilterCreate, db: Session = Depends(get_db)):
    return filter_crud.create_filter(db, filter_data)

@router.get("/", response_model=list[FilterOut])
def list_filters(db: Session = Depends(get_db)):
    return filter_crud.get_all_filters(db)
