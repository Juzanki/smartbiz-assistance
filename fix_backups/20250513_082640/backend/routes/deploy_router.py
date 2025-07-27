# backend/routes/deploy_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pathlib import Path

router = APIRouter()

class InjectRequest(BaseModel):
    tag: str
    code: str

@router.post("/inject-code")
def inject_code(data: InjectRequest):
    file_map = {
        "backend:fibonacci": "backend/routes/ai_functions.py",
        "backend:orders": "backend/routes/orders.py",
        # ongeza nyingine hapa...
    }

    if data.tag not in file_map:
        raise HTTPException(status_code=404, detail="Tag not found")

    path = Path(file_map[data.tag])
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# ==== GPT_INSERT_START [{data.tag}] ====\n# ==== GPT_INSERT_END [{data.tag}] ====\n")

    content = path.read_text()
    start_tag = f"# ==== GPT_INSERT_START [{data.tag}] ===="
    end_tag = f"# ==== GPT_INSERT_END [{data.tag}] ===="

    if start_tag not in content or end_tag not in content:
        raise HTTPException(status_code=400, detail="Tag markers missing")

    updated = content.replace(
        f"{start_tag}\n{end_tag}",
        f"{start_tag}\n{data.code}\n{end_tag}"
    )
    path.write_text(updated)
    return {"message": f"✅ Code injected for {data.tag}"}
