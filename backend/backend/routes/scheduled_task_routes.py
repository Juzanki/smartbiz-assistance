from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.models.user import User
from backend.auth import get_current_user
from backend.schemas.scheduled_task import ScheduledTaskCreate, ScheduledTaskOut
from backend.schemas.task_failure_log import TaskFailureLogOut
from backend.crud import scheduler_crud
from backend.crud import failure_log_crud

router = APIRouter(
    prefix="/scheduled-tasks",
    tags=["Scheduled Tasks"]
)

@router.post("/", response_model=ScheduledTaskOut)
def create_task(
    task: ScheduledTaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if task.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized to create for other users")
    return scheduler_crud.create_scheduled_task(db, task)

@router.get("/", response_model=List[ScheduledTaskOut])
def get_my_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(ScheduledTaskOut).filter(ScheduledTaskOut.user_id == current_user.id).all()

@router.get("/{task_id}/failures", response_model=List[TaskFailureLogOut])
def get_task_failures(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Optionally restrict access if needed
    logs = db.query(TaskFailureLogOut).filter(TaskFailureLogOut.task_id == task_id).all()
    return logs
