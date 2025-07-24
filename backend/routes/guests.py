from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.guest import GuestCreate, GuestOut
from backend.crud import guest_crud

router = APIRouter(prefix="/guests", tags=["Guests"])

@router.post("/", response_model=GuestOut)
def create_guest(data: GuestCreate, db: Session = Depends(get_db)):
    return guest_crud.create_guest(db, data)

@router.post("/{guest_id}/approve", response_model=GuestOut)
def approve_guest(guest_id: int, db: Session = Depends(get_db)):
    guest = guest_crud.approve_guest(db, guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@router.get("/room/{room_id}", response_model=list[GuestOut])
def get_guests_by_room(room_id: str, db: Session = Depends(get_db)):
    return guest_crud.get_guests_by_room(db, room_id)
