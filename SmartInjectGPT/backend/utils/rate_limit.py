# backend/utils/rate_limit.py

import time
import logging
from collections import defaultdict
from functools import wraps
from typing import Optional

from fastapi import Request, Depends
from fastapi.responses import JSONResponse

from backend.db import get_db
from backend.crud.rate_log_crud import create_rate_log
from backend.schemas.rate_log import APIRateLogCreate
from backend.auth.api_key import verify_admin_key  # ✅ Replaces get_api_key

# In-memory tracker (suggested: replace with Redis for production)
user_actions = defaultdict(list)

def check_rate(user: str, action: str, limit: int = 5, window_seconds: int = 60) -> bool:
    """
    Check if a user can perform an action within the rate limit.
    """
    key = f"{user}:{action}"
    now = time.time()
    window_start = now - window_seconds

    # Remove old entries
    user_actions[key] = [t for t in user_actions[key] if t > window_start]

    if len(user_actions[key]) >= limit:
        logging.warning(f"⛔ Rate limit hit for {key}")
        return False

    user_actions[key].append(now)
    return True

def rate_limited(limit: int = 5, window_seconds: int = 60):
    """
    FastAPI decorator for rate-limiting an endpoint and logging usage.
    Only accessible by trusted systems (uses X-Admin-Key via verify_admin_key).
    """
    def decorator(endpoint_func):
        @wraps(endpoint_func)
        async def wrapper(
            request: Request,
            admin=Depends(verify_admin_key),  # 🔐 Validate admin key
            db=Depends(get_db),
            *args,
            **kwargs
        ):
            action_key = f"{request.url.path}:{request.method}"
            admin_id = "admin-system"  # optional placeholder

            # Rate check
            if not check_rate(admin_id, action_key, limit, window_seconds):
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Too many requests. Try again later."}
                )

            # Process request
            response = await endpoint_func(request, *args, **kwargs)

            # Log metadata
            log_data = APIRateLogCreate(
                api_key_id=None,  # No actual API key object; using admin
                endpoint=request.url.path,
                method=request.method,
                status_code=getattr(response, "status_code", 200),
                ip_address=request.client.host
            )
            create_rate_log(db, log_data)

            return response
        return wrapper
    return decorator
