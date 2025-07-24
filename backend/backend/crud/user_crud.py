from datetime import datetime
from sqlalchemy.orm import Session
from backend.models import User, ScheduledMessage, SocialMediaPost
from backend.schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ========== AUTH HELPERS ==========

def get_user_by_identifier(db: Session, identifier: str):
    return db.query(User).filter(
        (User.email == identifier) |
        (User.username == identifier) |
        (User.phone_number == identifier)
    ).first()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_phone(db: Session, phone_number: str):
    return db.query(User).filter(User.phone_number == phone_number).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        phone_number=user.phone_number,
        full_name=user.full_name,
        password=hashed_password,
        subscription_status="free"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_profile(db: Session, user_id: int, updates: dict):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    for key, value in updates.items():
        if hasattr(user, key):
            setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

# ========== POSTS ==========

def get_user_posts(db: Session, user_id: int):
    return db.query(SocialMediaPost).filter(SocialMediaPost.user_id == user_id).all()

def create_post(db: Session, post_data: dict):
    post = SocialMediaPost(**post_data)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# ========== SCHEDULED MESSAGES ==========

def get_due_unsent_messages(db: Session):
    now = datetime.utcnow()
    return db.query(ScheduledMessage).filter(
        ScheduledMessage.sent == False,
        ScheduledMessage.scheduled_time <= now
    ).all()

def mark_as_sent(db: Session, message: ScheduledMessage):
    message.sent = True
    db.commit()
    db.refresh(message)
    return message
