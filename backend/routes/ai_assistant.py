# backend/routes/ai_assistant.py

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from backend.dependencies import get_current_user
from backend.models import User
import openai
import os
from typing import Optional

router = APIRouter(prefix="/ai-assistant", tags=["AI Assistant"])

# Load API Key securely from environment
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("OPENAI_API_KEY is missing in environment variables")

# ========== Request Schema ==========
class AIAssistantRequest(BaseModel):
    prompt: str = Field(..., example="Andika mpango wa biashara ya kuuza matunda mitandaoni.")
    language: str = Field(default="sw", example="sw", description="Lugha ya majibu (mfano: en, sw, fr)")

# ========== AI Assistant Endpoint ==========
@router.post("/ask", summary="💡 Tuma ombi kwa AI Assistant")
async def ask_ai(request: AIAssistantRequest,
                 current_user: User = Depends(get_current_user)):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")

    try:
        prompt = (
            f"You are a helpful Smart Business Assistant.\n"
            f"Respond in: {request.language}\n"
            f"User Email: {current_user.email}\n"
            f"Task: {request.prompt}"
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI business assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        reply = response.choices[0].message.content.strip()

        return {
            "user": current_user.email,
            "task": request.prompt,
            "language": request.language,
            "assistant_reply": reply
        }

    except openai.error.AuthenticationError:
        raise HTTPException(status_code=401, detail="Invalid or missing OpenAI API key.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Assistant Error: {str(e)}")
