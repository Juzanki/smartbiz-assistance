# smartinject.py — Backend route to execute AI kernel via frontend prompt

from fastapi import APIRouter
from pydantic import BaseModel
from backend.kernel.smartinject_kernel import SmartInjectKernel
from backend.firewall.prompt_firewall import scan_prompt_file
from backend.identity.soul_signature import verify_identity

router = APIRouter()

class PromptIn(BaseModel):
    prompt: str

@router.post("/api/smartinject/run")
def run_kernel(prompt: PromptIn):
    # Optional: Write prompt to a file (optional for memory log)
    with open("input_dream.txt", "w", encoding="utf-8") as f:
        f.write(prompt.prompt)

    if not verify_identity():
        return {"status": "❌", "message": "Soul verification failed"}

    scan = scan_prompt_file("input_dream.txt")
    if scan["status"] != "allowed":
        return {"status": "❌", "message": "Prompt blocked", "reason": scan["reason"]}

    SmartInjectKernel().run(prompt.prompt)
    return {"status": "✅", "message": "Kernel executed"}
