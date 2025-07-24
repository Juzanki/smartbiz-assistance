from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.db import get_db
from backend.auth import get_current_user
from backend.models.user import User
from backend.schemas.email_template import EmailTemplateCreate, EmailTemplateOut
from backend.crud import email_crud

router = APIRouter(
    prefix="/email-templates",
    tags=["Email Templates"]
)

@router.post("/", response_model=EmailTemplateOut)
def create_template(
    template: EmailTemplateCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin" and current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only admins can create templates")
    
    return email_crud.create_email_template(db, template)

@router.get("/", response_model=List[EmailTemplateOut])
def list_templates(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "admin" and current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only admins can view templates")
    
    return email_crud.get_all_templates(db)
