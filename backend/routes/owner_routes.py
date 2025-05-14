from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.auth import get_current_user
from backend.dependencies import check_owner_only, get_current_active_owner
from backend.models import User
from backend.schemas import RoleUpdateRequest, AdminCreate
from backend.utils.security import pwd_context

owner_router = APIRouter(
    prefix="/owner",
    tags=["Owner Management"]
)

# ==================== OWNER DASHBOARD ====================
@owner_router.get("/dashboard", summary="🛡️ Access Owner Dashboard")
def owner_dashboard(current_user: User = Depends(check_owner_only)):
    return {
        "message": f"👑 Karibu Owner: {current_user.full_name} ({current_user.email})",
        "role": current_user.role,
        "note": "Una nguvu ya kudhibiti mfumo mzima."
    }

# ==================== UPDATE USER ROLE ====================
@owner_router.post("/update-role", summary="🛠️ Owner can update user roles")
def update_user_role(
    payload: RoleUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(check_owner_only)
):
    user = db.query(User).filter(User.id == payload.user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.new_role not in ["user", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role provided.")

    user.role = payload.new_role
    db.commit()

    return {
        "message": f"✅ {user.email} is now a {user.role}"
    }

# ==================== ADD NEW ADMIN ====================
@owner_router.post("/admins", summary="➕ Add new admin",
                   dependencies=[Depends(get_current_active_owner)])
def add_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == admin.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")

    hashed = pwd_context.hash(admin.password)
    new_user = User(
        email=admin.email,
        full_name=admin.name,
        role="admin",
        password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"detail": f"✅ Admin '{admin.email}' created successfully."}

# ==================== LIST ALL ADMINS ====================
@owner_router.get("/admins", summary="📋 View all admins",
                  dependencies=[Depends(get_current_active_owner)])
def list_admins(db: Session = Depends(get_db)):
    admins = db.query(User).filter(User.role == "admin").all()
    return [
        {"email": admin.email, "name": admin.full_name}
        for admin in admins
    ]
