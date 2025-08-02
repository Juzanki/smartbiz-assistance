from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.recorded_stream_schemas import *
from backend.crud import recorded_stream_crud

router = APIRouter()

@router.post("/", response_model=RecordedStreamOut)
def upload_recording(data: RecordedStreamCreate, db: Session = Depends(get_db)):
    return recorded_stream_crud.create_recording(db, data)

@router.get("/stream/{stream_id}", response_model=RecordedStreamOut)
def get_recording(stream_id: int, db: Session = Depends(get_db)):
    recording = recorded_stream_crud.get_recording_by_stream(db, stream_id)
    if not recording:
        raise HTTPException(status_code=404, detail="Recording not found")
    return recording
