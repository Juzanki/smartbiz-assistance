from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from backend.db import get_db
from backend.models import User
from backend.dependencies import get_current_user
from sqlalchemy.orm import Session
import openai
import os

router = APIRouter(prefix="/owner", tags=["Owner AI Console"])


# ========== Schema ==========
class AICommandRequest(BaseModel):
    prompt: str = Field(..., example="Generate a report of system usage in the past 7 days")


class AICommandResponse(BaseModel):
    status: str
    output: str


# ========== Endpoint ==========
@router.post(
    "/command",
    response_model=AICommandResponse,
    summary="🧠 Execute AI Admin Command (Owner Only)"
)
def execute_owner_command(
    body: AICommandRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Allows the system owner to issue high-level AI-powered backend commands.
    Access is restricted to users with the `owner` role.
    """
    if current_user.role != "owner":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access restricted to owner only"
        )

    prompt = body.prompt.strip()
    if not prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Command prompt is required"
        )

    if not openai.api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="OpenAI API key is not set"
        )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a backend assistant with admin privileges."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=700
        )

        reply = response.choices[0].message.content.strip()
        return AICommandResponse(
            status="✅ Success",
            output=reply
        )

    except openai.error.AuthenticationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing OpenAI API key."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI processing error: {str(e)}"
        )
