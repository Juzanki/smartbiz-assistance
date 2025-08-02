from datetime import datetime
from pydantic import BaseModel

class TaskFailureLogBase(BaseModel):
    task_id: int
    error_message: str

class TaskFailureLogOut(TaskFailureLogBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
