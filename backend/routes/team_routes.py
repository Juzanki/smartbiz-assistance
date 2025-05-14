from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models import TeamMember, User
from backend.schemas import TeamMemberCreate, TeamMemberUpdate, TeamMemberOut
from backend.dependencies import get_current_user

router = APIRouter(prefix="/team", tags=["Team Management"])


# ========== GET TEAM MEMBERS ==========
@router.get("/members", response_model=List[TeamMemberOut], summary="👥 List team members")
def get_team_members(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(TeamMember).filter(TeamMember.owner_id == current_user.id).all()


# ========== ADD TEAM MEMBER ==========
@router.post("/add", response_model=TeamMemberOut, status_code=status.HTTP_201_CREATED, summary="➕ Add a new team member")
def add_team_member(
    payload: TeamMemberCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = db.query(TeamMember).filter(
        TeamMember.owner_id == current_user.id,
        TeamMember.email == payload.email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Team member already exists")

    new_member = TeamMember(owner_id=current_user.id, **payload.dict())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member


# ========== UPDATE TEAM MEMBER ==========
@router.put("/update/{member_id}", response_model=TeamMemberOut, summary="✏️ Update a team member")
def update_team_member(
    member_id: int,
    payload: TeamMemberUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(TeamMember).filter(
        TeamMember.id == member_id,
        TeamMember.owner_id == current_user.id
    ).first()

    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(member, field, value)

    db.commit()
    db.refresh(member)
    return member


# ========== REMOVE TEAM MEMBER ==========
@router.delete("/remove/{member_id}", status_code=status.HTTP_204_NO_CONTENT, summary="🗑️ Remove a team member")
def remove_team_member(
    member_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    member = db.query(TeamMember).filter(
        TeamMember.id == member_id,
        TeamMember.owner_id == current_user.id
    ).first()

    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")

    db.delete(member)
    db.commit()
    return None  # Required for 204 No Content
