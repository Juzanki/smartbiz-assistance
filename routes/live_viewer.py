from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.live_viewer import LiveViewer
from backend.schemas.live_viewer_schemas import LiveViewerIn, LiveViewerOut

router = APIRouter()

@router.post("/join", response_model=LiveViewerOut)
def join_stream(data: LiveViewerIn, db: Session = Depends(get_db)):
    existing = db.query(LiveViewer).filter_by(user_id=data.user_id, stream_id=data.stream_id, is_active=True).first()
    if existing:
        return existing
    viewer = LiveViewer(**data.dict())
    db.add(viewer)
    db.commit()
    db.refresh(viewer)
    return viewer

@router.post("/leave", response_model=LiveViewerOut)
def leave_stream(data: LiveViewerIn, db: Session = Depends(get_db)):
    viewer = db.query(LiveViewer).filter_by(user_id=data.user_id, stream_id=data.stream_id, is_active=True).first()
    if not viewer:
        raise HTTPException(status_code=404, detail="Viewer not found in active session")
    viewer.left_at = datetime.utcnow()
    viewer.is_active = False
    db.commit()
    db.refresh(viewer)
    return viewer
