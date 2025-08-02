from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import json
import os

router = APIRouter(prefix="/injector", tags=["SmartInjectGPT"])


# ========== Tafuta na Soma file_map.json ==========
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_MAP_PATH = os.path.join(BASE_DIR, "SmartInjectGPT", "scripts", "file_map.json")

try:
    with open(FILE_MAP_PATH, "r", encoding="utf-8-sig") as f:
        file_map = json.load(f)
except Exception as e:
    raise RuntimeError(f"❌ Failed to load file_map.json: {e}")


# ========== Schema ==========
class InjectRequest(BaseModel):
    tag: str
    response: str


# ========== Endpoint ==========
@router.post("/inject", summary="🚀 Inject response code into mapped file")
def inject_code(item: InjectRequest):
    """
    Injects the given response text into the file path mapped by the tag.
    Entire content of the file will be overwritten.
    """
    tag = item.tag.strip()
    if tag not in file_map:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid tag: {tag}"
        )

    target_path = file_map[tag]
    abs_path = os.path.abspath(target_path)

    try:
        # Prevent file path escape attempts
        if not abs_path.startswith(BASE_DIR):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid path. Access outside base directory is not allowed."
            )

        # Ensure directory exists
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        # Write content to file
        with open(abs_path, "w", encoding="utf-8") as f:
            f.write(item.response.strip())

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"⚠️ Failed to write file: {e}"
        )

    return {
        "message": f"✅ Code injected successfully into tag '{tag}'",
        "file": abs_path
    }
