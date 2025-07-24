from sqlalchemy.orm import Session
from backend.models.scheduled_task import ScheduledTask
from backend.schemas.scheduled_task import ScheduledTaskCreate
from datetime import datetime

def create_scheduled_task(db: Session, task: ScheduledTaskCreate):
    db_task = ScheduledTask(
        user_id=task.user_id,
        type=task.type,
        content=task.content,
        scheduled_time=task.scheduled_time,
        created_at=datetime.utcnow(),
        status="pending"
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_due_tasks(db: Session, current_time: datetime):
    return db.query(ScheduledTask).filter(
        ScheduledTask.scheduled_time <= current_time,
        ScheduledTask.status == "pending"
    ).all()

def update_task_status(db: Session, task_id: int, status: str, retry_count: int = 0):
    task = db.query(ScheduledTask).filter(ScheduledTask.id == task_id).first()
    if task:
        task.status = status
        task.retry_count = retry_count
        db.commit()
        db.refresh(task)
    return task
