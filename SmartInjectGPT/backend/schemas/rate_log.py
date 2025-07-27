from datetime import datetime
from pydantic import BaseModel

class APIRateLogCreate(BaseModel):
    endpoint: str
    method: str
    status_code: int
    ip_address: str
    api_key_id: int
    timestamp: datetime = datetime.utcnow()
