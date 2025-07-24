from pydantic import BaseModel
from datetime import datetime

class FilterCreate(BaseModel):
    name: str
    slug: str
    css_class: str

class FilterOut(BaseModel):
    id: int
    name: str
    slug: str
    css_class: str
    is_active: bool
    created_at: datetime
