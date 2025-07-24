from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.superchat import SuperchatCreate, SuperchatOut
from backend.crud import superchat_crud

router = APIRouter()

@router.post("/", response_model=SuperchatOut)
def send_superchat(sc: SuperchatCreate, db: Session = Depends(get_db)):
    return superchat_crud.create_superchat(db, sc)

@router.get("/{stream_id}", response_model=list[SuperchatOut])
def list_superchats(stream_id: str, db: Session = Depends(get_db)):
    return superchat_crud.get_superchats_by_stream(db, stream_id)
