from pydantic import BaseModel
from datetime import datetime

class CoHostInviteCreate(BaseModel):
    stream_id: str
    host_id: int
    invitee_id: int

class CoHostInviteOut(BaseModel):
    id: int
    stream_id: str
    host_id: int
    invitee_id: int
    status: str
    sent_at: datetime
