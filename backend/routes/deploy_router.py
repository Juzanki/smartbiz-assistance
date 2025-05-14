# backend/routes/deploy_router.py

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from pathlib import Path

router = APIRouter(tags=["Code Deployment"])


# ========== Request Schema ==========
class InjectRequest(BaseModel):
    tag: str
    code: str


# ========== File Map ==========
FILE_MAP = {
    "backend:fibonacci": "backend/routes/ai_functions.py",
    "backend:orders": "backend/routes/orders.py",
    # 💡 Ongeza tags zingine hapa...
}


# ========== Inject Code Endpoint ==========
@router.post("/inject-code", summary="🧠 Inject code into mapped files")
def inject_code(data: InjectRequest):
    if data.tag not in FILE_MAP:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tag '{data.tag}' not found in file_map."
        )

    path = Path(FILE_MAP[data.tag])
    start_tag = f"# ==== GPT_INSERT_START [{data.tag}] ===="
    end_tag = f"# ==== GPT_INSERT_END [{data.tag}] ===="

    # Auto-create file with default tag structure if not found
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{start_tag}\n{end_tag}\n")

    content = path.read_text()

    if start_tag not in content or end_tag not in content:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Missing tag markers for '{data.tag}' in file."
        )

    # Safely replace code block
    new_block = f"{start_tag}\n{data.code.strip()}\n{end_tag}"
    updated = content.replace(
        f"{start_tag}\n{end_tag}",
        new_block
    )

    path.write_text(updated)

    return {
        "message": f"✅ Code injected successfully for tag: {data.tag}",
        "file": str(path)
    }
