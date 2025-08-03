from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.user_bot import UserBot
from backend.schemas.user_bot_schemas import UserBotCreate, UserBotOut
from typing import List

router = APIRouter()

@router.post("/", response_model=UserBotOut)
def create_user_bot(bot: UserBotCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    new_bot = UserBot(
        name=bot.name,
        purpose=bot.purpose,
        bot_package_id=bot.bot_package_id,
        user_id=current_user["id"],
        expiry_date=None
    )
    db.add(new_bot)
    db.commit()
    db.refresh(new_bot)
    return new_bot

@router.get("/my", response_model=List[UserBotOut])
def get_my_bots(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    return db.query(UserBot).filter(UserBot.user_id == current_user["id"]).all()
