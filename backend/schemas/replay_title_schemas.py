from pydantic import BaseModel

class ReplayTitleCreate(BaseModel):
    stream_id: int
    generated_title: str

class ReplayTitleOut(BaseModel):
    id: int
    stream_id: int
    generated_title: str

    class Config:
        orm_mode = True
