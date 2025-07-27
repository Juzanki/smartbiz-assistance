from fastapi import Depends
from backend.dependencies.api_auth import require_api_key
from backend.dependencies.rate_limit import check_rate_limit

@router.post("/infer")
def infer(request: InferenceRequest, api_key=Depends(require_api_key)):
    check_rate_limit(api_key)  # 🔐 Hii hapa ndio kizuizi kwa plan usage
    ...
