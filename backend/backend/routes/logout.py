"""
Logout endpoint for SmartBiz Assistant.
Handles logging out users by blacklisting JWT tokens in memory.
"""

from datetime import datetime
from typing import Set

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from backend.utils.security import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/auth/logout", tags=["Authentication"])

# ========== In-Memory Token Blacklist ==========
blacklisted_tokens: Set[str] = set()

# OAuth2 Scheme for extracting token from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/", summary="🚪 Logout and blacklist JWT token")
def logout_user(token: str = Depends(oauth2_scheme)):
    """
    Blacklists the current user's JWT access token.
    This prevents it from being reused in protected routes.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get("exp")

        if not exp:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token is missing expiration timestamp."
            )

        if datetime.utcnow().timestamp() > exp:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has already expired."
            )

        # Add token to in-memory blacklist
        blacklisted_tokens.add(token)
        return {"message": "✅ Logout successful. Token has been invalidated."}

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or malformed token."
        )


def verify_not_blacklisted(token: str = Depends(oauth2_scheme)) -> str:
    """
    Dependency to ensure the token has not been blacklisted (i.e. user is not logged out).
    Recommended to use in get_current_user chain.
    """
    if token in blacklisted_tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been invalidated due to logout."
        )
    return token
