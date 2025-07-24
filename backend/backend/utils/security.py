"""
🔐 Security utilities for SmartBiz Assistance SaaS.
Handles password hashing, JWT token generation and decoding securely.
"""

import os
from datetime import datetime, timedelta
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext

# ==================== LOAD ENVIRONMENT VARIABLES ====================
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("❌ SECRET_KEY not found in environment variables!")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# ==================== PASSWORD HASHING ====================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Hash a plain password using bcrypt.
    Raises ValueError if password is empty.
    """
    if not password or not password.strip():
        raise ValueError("❌ Password to hash cannot be empty!")
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    Returns True if match, otherwise False.
    """
    if not plain_password or not hashed_password:
        return False
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception:
        return False

# ==================== JWT TOKEN CREATION ====================

def create_access_token(
    data: Dict[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a signed JWT token for authentication.
    - `data` should contain unique identifier e.g. {"sub": user_id}
    - `expires_delta` is optional (default: 60 minutes)
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ==================== JWT TOKEN DECODING ====================

def decode_access_token(token: str) -> Dict[str, Any]:
    """
    Decode a JWT token and return the payload.
    Raises ValueError if the token is invalid or expired.
    """
    if not token:
        raise ValueError("Token is required")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise ValueError(f"❌ Invalid or expired token: {e}") from e
