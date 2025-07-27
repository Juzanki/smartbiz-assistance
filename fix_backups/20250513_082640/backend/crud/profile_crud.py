from sqlalchemy.orm import Session
from backend.models import User
from backend.schemas.user import UserUpdate

# --- Get Profile ---
def get_user_profile(db: Session, user_id: int) -> User:
    return db.query(User).filter(User["id"]== user_id).first()

# --- Update Profile ---
def update_user_profile(db: Session, user_id: int, data: UserUpdate) -> User:
    user = db.query(User).filter(User["id"]== user_id).first()
    if user:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(user, field, value)
        db.commit()
        db.refresh(user)
    return user
