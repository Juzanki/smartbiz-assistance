from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os

router = APIRouter()

# Tafuta file_map.json vizuri
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_MAP_PATH = os.path.join(BASE_DIR, "SmartInjectGPT", "scripts", "file_map.json")

# Soma file_map kwa utf-8-sig (kuzuia BOM error)
try:
    with open(FILE_MAP_PATH, "r", encoding="utf-8-sig") as f:
        file_map = json.load(f)
except Exception as e:
    raise RuntimeError(f"⚠️ file_map.json could not be loaded: {e}")

class InjectRequest(BaseModel):
    tag: str
    response: str

@router.post("/inject")
def inject_code(item: InjectRequest):
    if item.tag not in file_map:
        raise HTTPException(status_code=400, detail=f"Invalid tag: {item.tag}")

    target_path = file_map[item.tag]
    abs_path = os.path.abspath(target_path)

    try:
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(item.response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write file: {e}")

    return {"message": f"✅ Code injected successfully into '{item.tag}'"}
