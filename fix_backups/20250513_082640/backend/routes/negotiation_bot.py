import os
import logging
from dotenv import load_dotenv
import openai
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from backend.auth import get_current_user
from backend.models import User
from backend.utils.access_control import require_plan

# ========== Setup ==========
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

logger = logging.getLogger(__name__)
router = APIRouter()

class NegotiationPrompt(BaseModel):
    customer_message: str

@router.post(
    "/ai/negotiate",
    summary="AI Negotiation Bot for SmartBiz",
    dependencies=[Depends(require_plan(["Pro", "Business"]))],
)
def negotiate_response(
    request: NegotiationPrompt,
    current_user: User = Depends(get_current_user)
):
    prompt = request.customer_message.strip()

    if not prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer message cannot be empty."
        )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a business assistant skilled in negotiation."},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content.strip()

        return {
            "response": answer,
            "customer_input": prompt,
            "negotiator": current_user.email
        }

    except Exception as exc:
        logger.exception("❌ OpenAI Error: %s", str(exc))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Negotiation bot failed. Check OpenAI setup."
        ) from exc
