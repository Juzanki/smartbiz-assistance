from sqlalchemy.orm import Session
from backend.models import User
from backend.schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_identifier(db: Session, identifier: str):
    return db.query(User).filter(
        (User.email == identifier) |
        (User.username == identifier) |
        (User.phone_number == identifier)
    ).first()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User["id"]== user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        phone_number=user.phone_number,
        full_name=user.full_name,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_phone(db: Session, phone_number: str):
    return db.query(User).filter(User.phone_number == phone_number).first()

def update_user_profile(db: Session, user_id: int, updates: dict):
    user = db.query(User).filter(User["id"]== user_id).first()
    if not user:
        return None

    for key, value in updates.items():
        if hasattr(user, key):
            setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user

def create_post(db: Session, user_id: int, post_data: dict):
    # Placeholder function - customize this if you have a Post model
    # For now, this just returns the input for testing
    return {
        "user_id": user_id,
        "status": "Post created",
        "data": post_data
    }

def get_user_posts(db: Session, user_id: int):
    # Placeholder: customize if you have a Post model
    return [
        {"post_id": 1, "title": "Post ya Kwanza", "user_id": user_id},
        {"post_id": 2, "title": "Post ya Pili", "user_id": user_id}
    ]

def create_scheduled_message(db: Session, user_id: int, message_data: dict):
    # Placeholder: Customize if you have a ScheduledMessage model
    return {
        "user_id": user_id,
        "status": "Scheduled message created",
        "message": message_data
    }
def get_user_scheduled_messages(db: Session, user_id: int):
    # Placeholder response – customize based on your ScheduledMessage model
    return [
        {"message_id": 1, "status": "pending", "user_id": user_id},
        {"message_id": 2, "status": "sent", "user_id": user_id}
    ]
def get_due_unsent_messages(db: Session):
    # Placeholder: Customize this with actual logic if using a ScheduledMessage model
    return [
        {"message_id": 1, "status": "pending", "send_time": "2025-05-13T09:00:00"},
        {"message_id": 2, "status": "pending", "send_time": "2025-05-13T10:30:00"}
    ]
def mark_as_sent(db: Session, message_id: int):
    # Placeholder logic: Replace with actual ScheduledMessage update logic
    return {
        "message_id": message_id,
        "status": "marked as sent"
    }
