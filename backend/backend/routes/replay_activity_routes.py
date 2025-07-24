from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.replay_activity_schemas import ReplayActivityIn, ReplayActivityOut
from backend.dependencies import get_db, get_current_user_optional
from backend.crud import replay_activity_crud

router = APIRouter()

@router.post("/{video_post_id}", response_model=ReplayActivityOut)
def log_replay_activity(video_post_id: int, data: ReplayActivityIn, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_optional)):
    return replay_activity_crud.log_activity(db, user_id, video_post_id, data.action, data.platform)
