from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.post("/suggest-title")
def suggest_title(events: List[str]):
    if "big gift" in events:
        return {"suggested_title": "?? Gift Rain Show"}
    elif "peak moment" in events:
        return {"suggested_title": "?? Peak Power"}
    return {"suggested_title": "?? SmartBiz Replay"}
