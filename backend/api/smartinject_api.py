from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import json

router = APIRouter()


class InjectionRequest(BaseModel):
    tag: str
    response: str


@router.post("/inject")
def inject_code(req: InjectionRequest):
    try:
        # Tafuta path ya file_map.json kwa usahihi
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_map_path = os.path.join(base_dir, "..", "file_map.json")
        file_map_path = os.path.abspath(file_map_path)

        if not os.path.exists(file_map_path):
            raise HTTPException(
                status_code=404,
                detail="❌ file_map.json not found")

        # Soma file_map.json
        with open(file_map_path, "r", encoding="utf-8") as f:
            file_map = json.load(f)

        if req.tag not in file_map:
            raise HTTPException(
                status_code=404,
                detail=f"❌ Tag '{req.tag}' not found in file_map")

        # Tafuta mahali pa kuweka code
        target_relative_path = file_map[req.tag]
        target_file_path = os.path.abspath(
            os.path.join(os.getcwd(), target_relative_path))

        # Hakikisha folder lipo
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        # Andika response kwenye faili
        with open(target_file_path, "w", encoding="utf-8") as f:
            f.write(req.response)

        return {"message": f"✅ Code successfully injected to {target_relative_path}"}

    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"💥 Injection failed: {str(e)}")
