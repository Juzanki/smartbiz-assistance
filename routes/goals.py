from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.goal import GoalCreate, GoalOut
from backend.crud import goal_crud
from backend.db import get_db

router = APIRouter(prefix="/goals", tags=["Goals"])

@router.post("/", response_model=GoalOut)
def create_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    return goal_crud.create_goal(db, goal)

@router.get("/", response_model=list[GoalOut])
def list_goals(db: Session = Depends(get_db)):
    return goal_crud.get_all_goals(db)

@router.put("/{goal_id}/update", response_model=GoalOut)
def update_goal(goal_id: int, amount: float, db: Session = Depends(get_db)):
    goal = goal_crud.update_goal_progress(db, goal_id, amount)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal

@router.delete("/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = goal_crud.delete_goal(db, goal_id)
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return {"detail": "Goal deleted"}
