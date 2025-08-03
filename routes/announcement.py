from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.announcement import AnnouncementCreate, AnnouncementOut
from backend.crud import announcement as announcement_crud

router = APIRouter()

@router.post("/", response_model=AnnouncementOut)
def create_announcement(data: AnnouncementCreate, db: Session = Depends(get_db)):
    return announcement_crud.create_announcement(db, data)

@router.get("/", response_model=list[AnnouncementOut])
def list_announcements(db: Session = Depends(get_db)):
    return announcement_crud.get_announcements(db)
