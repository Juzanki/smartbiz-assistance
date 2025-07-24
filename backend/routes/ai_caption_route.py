from fastapi import APIRouter
from backend.schemas.ai_caption_schemas import CaptionRequest

router = APIRouter()

@router.post("/caption-ai")
def generate_caption(data: CaptionRequest):
    # MOCK AI logic (replace with whisper or external service)
    return {
        "timestamp": data.timestamp,
        "caption": f"AI caption at {data.timestamp} from video."
    }
