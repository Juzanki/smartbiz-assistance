from sqlalchemy.orm import Session
from backend.models import StreamGuest
from typing import List

# --- Add Guest to Livestream ---
def add_guest(db: Session, stream_id: int, user_id: int) -> StreamGuest:
    guest = StreamGuest(stream_id=stream_id, user_id=user_id)
    db.add(guest)
    db.commit()
    db.refresh(guest)
    return guest

# --- Remove Guest ---
def remove_guest(db: Session, stream_id: int, user_id: int) -> bool:
    guest = db.query(StreamGuest).filter(StreamGuest.stream_id == stream_id, StreamGuest.user_id == user_id).first()
    if guest:
        db.delete(guest)
        db.commit()
        return True
    return False

# --- Get Guests for a Stream ---
def get_stream_guests(db: Session, stream_id: int) -> List[StreamGuest]:
    return db.query(StreamGuest).filter(StreamGuest.stream_id == stream_id).all()
