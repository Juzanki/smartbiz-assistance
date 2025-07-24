from pydantic import BaseModel

class StreamSettingsBase(BaseModel):
    camera_on: bool
    mic_on: bool

class StreamSettingsCreate(StreamSettingsBase):
    stream_id: int

class StreamSettingsUpdate(StreamSettingsBase):
    pass

class StreamSettingsOut(StreamSettingsBase):
    id: int
    stream_id: int

    class Config:
        orm_mode = True
