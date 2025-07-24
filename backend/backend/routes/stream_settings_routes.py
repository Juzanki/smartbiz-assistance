from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.schemas.stream_settings_schemas import *
from backend.crud import stream_settings_crud

router = APIRouter()

@router.get("/{stream_id}", response_model=StreamSettingsOut)
def get_stream_settings(stream_id: int, db: Session = Depends(get_db)):
    settings = stream_settings_crud.get_settings(db, stream_id)
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings

@router.post("/{stream_id}", response_model=StreamSettingsOut)
def update_stream_settings(stream_id: int, data: StreamSettingsUpdate, db: Session = Depends(get_db)):
    return stream_settings_crud.create_or_update_settings(db, stream_id, data)
