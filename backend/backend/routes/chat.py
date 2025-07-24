from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import ChatCreate, ChatOut
from backend.crud.chat_crud import create_message, get_messages_by_room
from backend.db import get_db

router = APIRouter(prefix="/chat", tags=["Chat"])

# 📨 Tuma ujumbe mpya
@router.post("/", response_model=ChatOut)
def send_message(chat: ChatCreate, db: Session = Depends(get_db)):
    msg = create_message(db, chat)
    return ChatOut.from_orm(msg)  # 🧼 Clean + auto

# 📥 Pata ujumbe wa chumba fulani
@router.get("/{room_id}", response_model=list[ChatOut])
def get_room_messages(room_id: str, db: Session = Depends(get_db)):
    messages = get_messages_by_room(db, room_id)
    return [ChatOut.from_orm(msg) for msg in messages]
