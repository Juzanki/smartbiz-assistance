from fastapi import Body

@router.post("/upgrade-plan")
def upgrade_plan(
    plan: str = Body(..., embed=True),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    key = db.query(APIKey).filter(APIKey.user_id == current_user.id).first()
    if not key:
        raise HTTPException(status_code=404, detail="No API key found")

    if plan not in ["free", "pro", "enterprise"]:
        raise HTTPException(status_code=400, detail="Invalid plan selected")

    key.plan = plan
    db.commit()
    return {
        "message": f"Plan upgraded to {plan}",
        "new_plan": key.plan
    }
