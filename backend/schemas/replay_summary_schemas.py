from pydantic import BaseModel

class ReplaySummaryCreate(BaseModel):
    stream_id: int
    summary_text: str

class ReplaySummaryOut(BaseModel):
    id: int
    stream_id: int
    summary_text: str

    class Config:
        orm_mode = True
