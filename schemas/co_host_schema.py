from pydantic import BaseModel
from datetime import datetime

# ✅ CoHost creation schema
class CoHostCreate(BaseModel):
    stream_id: str
    user_id: int

# ✅ CoHost output schema without orm_mode
class CoHostOut(BaseModel):
    id: int
    stream_id: str
    user_id: int
    status: str
    created_at: datetime

    @staticmethod
    def from_model(obj):
        return CoHostOut(
            id=obj.id,
            stream_id=obj.stream_id,
            user_id=obj.user_id,
            status=obj.status,
            created_at=obj.created_at
        )
