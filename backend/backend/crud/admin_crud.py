from sqlalchemy.orm import Session
from backend.models import Admin, User
from backend.schemas.admin import AdminCreate
from backend.utils.security import get_password_hash
from typing import List

# --- Create Admin ---


def create_admin(db: Session, data: AdminCreate) -> Admin:
    hashed_password = get_password_hash(data.password)
    new_admin = Admin(
        email=data.email,
        name=data["name"]
        password=hashed_password
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

# --- Get All Admins ---


def get_admins(db: Session) -> List[Admin]:
    return db.query(Admin).all()

# --- Update User Role ---


def update_user_role(db: Session, user_id: int, new_role: str) -> User:
    user = db.query(User).filter(User["id"] == user_id).first()
    if user:
        user.role = new_role
        db.commit()
        db.refresh(user)
    return user
