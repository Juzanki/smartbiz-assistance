# backend/routes/ai_responder.py

import os
import openai
import httpx
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from backend.auth import get_current_user
from backend.models import User


router = APIRouter(prefix="/ai", tags=["AI Assistant"])

# Load API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

openai.api_key = OPENAI_API_KEY


class AIRequest(BaseModel):
    prompt: str


@router.post("/respond", summary="🤖 Smart AI Responder")
async def ai_respond(request: AIRequest, current_user: User = Depends(get_current_user)):
    prompt = request.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    # 1. Try OpenAI
    if OPENAI_API_KEY:
        try:
            response = openai.ChatCompletion.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return {"source": "openai", "response": response.choices[0].message.content.strip()}
        except Exception as e:
            print("⚠️ OpenAI failed:", str(e))

    # 2. Try DeepSeek
    if DEEPSEEK_API_KEY:
        try:
            headers = {
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
            }
            async with httpx.AsyncClient() as client:
                resp = await client.post("https://api.deepseek.com/v1/chat/completions", json=payload, headers=headers)
                result = resp.json()
                return {"source": "deepseek", "response": result["choices"][0]["message"]["content"].strip()}
        except Exception as e:
            print("⚠️ DeepSeek failed:", str(e))

    # 3. Try HuggingFace
    if HUGGINGFACE_API_TOKEN:
        try:
            headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
            data = {"inputs": prompt}
            async with httpx.AsyncClient() as client:
                resp = await client.post("https://api-inference.huggingface.co/models/google/flan-t5-large", json=data, headers=headers)
                result = resp.json()
                return {"source": "huggingface", "response": result[0]["generated_text"].strip()}
        except Exception as e:
            print("⚠️ HuggingFace failed:", str(e))

    # 4. All failed
    raise HTTPException(status_code=500, detail="All AI services failed or not configured.")
