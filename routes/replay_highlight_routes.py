from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.replay_highlight_schemas import ReplayHighlightCreate, ReplayHighlightOut
from backend.dependencies import get_db
from backend.crud import replay_highlight_crud

router = APIRouter()

@router.post("/{video_post_id}", response_model=ReplayHighlightOut)
def add_highlight(video_post_id: int, data: ReplayHighlightCreate, db: Session = Depends(get_db)):
    return replay_highlight_crud.create_highlight(db, video_post_id, data.title, data.timestamp)

@router.get("/{video_post_id}", response_model=list[ReplayHighlightOut])
def get_highlight_list(video_post_id: int, db: Session = Depends(get_db)):
    return replay_highlight_crud.get_highlights(db, video_post_id)
