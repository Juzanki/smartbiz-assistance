# creator_routes.py — SmartCreatorAI Feature Generator API

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from SmartInjectGPT.creator.smart_creator_kernel import SmartCreatorKernel

router = APIRouter(prefix="/creator", tags=["SmartCreator"])

kernel = SmartCreatorKernel()

class FeaturePrompt(BaseModel):
    prompt: str

@router.post("/generate-feature")
def generate_feature(data: FeaturePrompt):
    try:
        result = kernel.create_feature_from_prompt(data.prompt)
        return {
            "status": "success",
            "feature": result["feature"],
            "progress": result["progress"],
            "suggestions": result["suggestions"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
