from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.co_host_invite import CoHostInvite
from backend.schemas.co_host_invite import CoHostInviteCreate, CoHostInviteOut
from typing import List

router = APIRouter(
    prefix="/co-host-invites",
    tags=["CoHost Invites"]
)

# ✅ Create an invite
@router.post("/", response_model=CoHostInviteOut)
def send_invite(data: CoHostInviteCreate, db: Session = Depends(get_db)):
    invite = CoHostInvite(**data.dict())
    db.add(invite)
    db.commit()
    db.refresh(invite)
    return invite

# ✅ Get invites for a specific invitee
@router.get("/invitee/{user_id}", response_model=List[CoHostInviteOut])
def get_user_invites(user_id: int, db: Session = Depends(get_db)):
    return db.query(CoHostInvite).filter(CoHostInvite.invitee_id == user_id).order_by(CoHostInvite.sent_at.desc()).all()

# ✅ Update invite status (accept/reject)
@router.put("/{invite_id}/status", response_model=CoHostInviteOut)
def update_invite_status(invite_id: int, status: str, db: Session = Depends(get_db)):
    invite = db.query(CoHostInvite).filter(CoHostInvite.id == invite_id).first()
    if not invite:
        raise HTTPException(status_code=404, detail="Invite not found")
    invite.status = status
    db.commit()
    db.refresh(invite)
    return invite

# ✅ Delete an invite
@router.delete("/{invite_id}")
def delete_invite(invite_id: int, db: Session = Depends(get_db)):
    invite = db.query(CoHostInvite).filter(CoHostInvite.id == invite_id).first()
    if not invite:
        raise HTTPException(status_code=404, detail="Invite not found")
    db.delete(invite)
    db.commit()
    return {"message": "Invite deleted"}
