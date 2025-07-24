from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.bot_package import BotPackage
from backend.schemas.bot_package_schemas import BotPackageOut
import json

router = APIRouter()

@router.get("/", response_model=List[BotPackageOut])
def get_all_bot_packages(db: Session = Depends(get_db)):
    packages = db.query(BotPackage).all()
    for pkg in packages:
        pkg.features = json.loads(pkg.features)
    return packages
