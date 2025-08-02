from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.comment_schemas import VideoCommentCreate, VideoCommentOut
from backend.crud import comment_crud
from backend.dependencies import get_db, get_current_user
from backend.models.user import User

router = APIRouter()

@router.post("/", response_model=VideoCommentOut)
def post_comment(data: VideoCommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return comment_crud.create_comment(db, current_user.id, data)

@router.get("/video/{video_post_id}", response_model=list[VideoCommentOut])
def get_comments(video_post_id: int, db: Session = Depends(get_db)):
    return comment_crud.get_comments_by_video(db, video_post_id)

@router.delete("/{comment_id}", response_model=dict)
def delete_comment(comment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted = comment_crud.delete_comment(db, comment_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Comment not found or unauthorized")
    return {"detail": "Comment deleted"}
