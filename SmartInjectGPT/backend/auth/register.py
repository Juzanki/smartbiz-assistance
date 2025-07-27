from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, constr
from backend.dependencies import get_db
from backend.models.user import User
from backend.school.hash_password import hash_password, verify_password

router = APIRouter()

# === Schemas ===
class RegisterSchema(BaseModel):
    username: constr(strip_whitespace=True, min_length=3)
    email: EmailStr
    password: constr(min_length=6)

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

# === Register Route ===
@router.post("/register")
def register(user_input: RegisterSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user_input.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user_input.password)
    new_user = User(
        username=user_input.username,
        email=user_input.email,
        password_hash=hashed_pw,
        role="user"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"🎉 Welcome, {new_user.username}!"}

# === Login Route ===
@router.post("/login")
def login(user_input: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_input.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user_input.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": f"✅ Welcome, {user.username}!"}
