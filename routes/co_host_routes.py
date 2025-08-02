from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.schemas.co_host_schema import CoHostCreate, CoHostOut
from backend.models.co_host import CoHost
from backend.db import get_db

router = APIRouter()  # ✅ Hii ilikuwa imekosekana!

@router.post("/invite", response_model=CoHostOut)
def invite_cohost(data: CoHostCreate, db: Session = Depends(get_db)):
    new_invite = CoHost(**data.dict())
    db.add(new_invite)
    db.commit()
    db.refresh(new_invite)
    return CoHostOut.from_model(new_invite)  # 👈 kama hutumii orm_mode

@router.get("/list/{stream_id}", response_model=List[CoHostOut])
def get_cohosts(stream_id: str, db: Session = Depends(get_db)):
    results = db.query(CoHost).filter(CoHost.stream_id == stream_id).all()
    return [CoHostOut.from_model(i) for i in results]

@router.put("/update/{cohost_id}", response_model=CoHostOut)
def update_cohost(cohost_id: int, status: str, db: Session = Depends(get_db)):
    invite = db.query(CoHost).filter(CoHost.id == cohost_id).first()
    invite.status = status
    db.commit()
    return CoHostOut.from_model(invite)
