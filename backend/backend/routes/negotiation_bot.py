import os
import logging
from dotenv import load_dotenv
import openai
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from backend.auth import get_current_user
from backend.models import User
from backend.utils.access_control import require_plan

# ========== Setup ==========
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("❌ OPENAI_API_KEY not found in environment.")

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/ai", tags=["AI Negotiation Bot"])


# ========== Schema ==========
class NegotiationPrompt(BaseModel):
    customer_message: str = Field(..., example="Can I get a discount if I buy 10 units?")
    language: str = Field(default="en", example="en", description="Response language (e.g. en, sw, fr)")


# ========== Endpoint ==========
@router.post(
    "/negotiate",
    summary="🧠 Smart Negotiation Assistant (Pro/Business only)",
    dependencies=[Depends(require_plan(["Pro", "Business"]))],
)
def negotiate_response(
    request: NegotiationPrompt,
    current_user: User = Depends(get_current_user)
):
    """
    Generate a smart negotiation reply based on customer input.
    Only accessible by users on Pro or Business plans.
    """
    prompt = request.customer_message.strip()

    if not prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer message cannot be empty."
        )

    try:
        system_prompt = (
            f"You are a skilled business assistant who helps respond to customer negotiations "
            f"in {request.language.upper()} in a polite and persuasive way."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        answer = response.choices[0].message.content.strip()

        return {
            "customer_input": prompt,
            "response": answer,
            "negotiator": current_user.email,
            "language": request.language
        }

    except openai.error.AuthenticationError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing OpenAI API key."
        )
    except Exception as exc:
        logger.exception("❌ OpenAI Error: %s", str(exc))
        raise HTTPException(
            status_code=500,
            detail="Negotiation bot failed to respond."
        ) from exc
