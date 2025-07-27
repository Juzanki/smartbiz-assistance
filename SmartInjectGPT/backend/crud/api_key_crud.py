from sqlalchemy.orm import Session
from backend.models.api_key import APIKey
from backend.schemas.api_key import APIKeyCreate
from datetime import datetime

def get_api_key_by_key(db: Session, key: str):
    return db.query(APIKey).filter(APIKey.key == key).first()

def create_api_key(db: Session, api_key_data: APIKeyCreate):
    db_key = APIKey(
        key=api_key_data.key,
        owner_id=api_key_data.owner_id,
        plan=api_key_data.plan,
        created_at=datetime.utcnow()
    )
    db.add(db_key)
    db.commit()
    db.refresh(db_key)
    return db_key

def delete_api_key(db: Session, key: str):
    db_key = get_api_key_by_key(db, key)
    if db_key:
        db.delete(db_key)
        db.commit()
    return db_key

def list_all_api_keys(db: Session, skip: int = 0, limit: int = 100):
    return db.query(APIKey).offset(skip).limit(limit).all()
