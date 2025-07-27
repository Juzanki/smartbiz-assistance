from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.auth import get_current_user
from backend.models.user import User
import os, json

router = APIRouter(prefix="/developer", tags=["Developer"])

MODEL_DIR = "models/custom/"

@router.get("/models")
def get_trained_models(current_user: User = Depends(get_current_user)):
    models = []
    for file in os.listdir(MODEL_DIR):
        if file.endswith(".meta.json"):
            path = os.path.join(MODEL_DIR, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                    if meta["trained_by"] == current_user.username:
                        models.append(meta)
            except:
                continue
    return JSONResponse(content=models)
