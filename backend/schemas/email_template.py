from datetime import datetime
from pydantic import BaseModel

class EmailTemplateBase(BaseModel):
    name: str
    subject: str
    html_content: str

class EmailTemplateCreate(EmailTemplateBase):
    pass

class EmailTemplateOut(EmailTemplateBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
