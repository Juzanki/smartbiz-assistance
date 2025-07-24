from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.like_model import Like
from backend.schemas.like_schema import LikeCreate, LikeResponse

router = APIRouter(
    prefix="/likes",
    tags=["Likes"]
)

@router.post("/", response_model=LikeResponse, status_code=status.HTTP_201_CREATED)
def add_like(like_data: LikeCreate, db: Session = Depends(get_db)):
    """
    Add a new like to a stream.
    """
    try:
        like = Like(**like_data.dict())
        db.add(like)
        db.commit()
        db.refresh(like)
        return like
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding like: {str(e)}")


@router.get("/count/{stream_id}")
def get_like_count(stream_id: str, db: Session = Depends(get_db)):
    """
    Get total number of likes for a specific stream.
    """
    try:
        count = db.query(Like).filter(Like.stream_id == stream_id).count()
        return {"stream_id": stream_id, "likes": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching like count: {str(e)}")
