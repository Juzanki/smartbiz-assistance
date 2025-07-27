from pydantic import BaseModel, Field, constr

# --- ForgotPasswordRequest ---
class ForgotPasswordRequest(BaseModel):
    identifier: str = Field(..., example="juza@example.com or +255712345678")

# --- VerifyResetCode ---
class VerifyResetCode(BaseModel):
    identifier: str
    code: str

# --- ResetPassword ---
class ResetPassword(BaseModel):
    identifier: str
    code: str
    new_password: constr(min_length=6)
