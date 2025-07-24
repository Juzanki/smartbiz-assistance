# backend/routes/host_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.host_schemas import CoHostInviteCreate, CoHostInviteOut, CoHostInviteUpdate
from backend.crud import host_crud
from backend.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/invite", response_model=CoHostInviteOut)
def send_invite(invite: CoHostInviteCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return host_crud.create_invite(db, sender_id=user.id, invite=invite)

@router.put("/invite/{invite_id}", response_model=CoHostInviteOut)
def respond_invite(invite_id: int, update: CoHostInviteUpdate, db: Session = Depends(get_db)):
    return host_crud.update_invite_status(db, invite_id, update.status)

@router.get("/invites/{stream_id}", response_model=List[CoHostInviteOut])
def list_invites(stream_id: int, db: Session = Depends(get_db)):
    return host_crud.get_stream_invites(db, stream_id)
