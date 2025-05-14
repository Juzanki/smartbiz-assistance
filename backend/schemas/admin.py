from pydantic import BaseModel, EmailStr

# --- RoleUpdateRequest ---


class RoleUpdateRequest(BaseModel):
    user_id: int
    new_role: str

# --- AdminCreate ---


class AdminCreate(BaseModel):
    email: str
    password: str
    name: str

# --- OwnerLoginRequest ---


class OwnerLoginRequest(BaseModel):
    email: EmailStr

# --- OwnerLoginVerify ---


class OwnerLoginVerify(BaseModel):
    token: str
