from fastapi import HTTPException
from datetime import datetime, timedelta

# Sample daily plan limits
API_PLANS = {
    "free": 100,
    "pro": 1000,
    "enterprise": None  # No limit
}

# In-memory tracker (can be replaced with Redis or DB for production)
rate_limit_cache = {}

def check_rate_limit(api_key_obj):
    """
    Checks if the given API key has exceeded the daily usage limit based on its plan.
    """
    plan = getattr(api_key_obj, "plan", "free")  # Default to free plan if not set
    key_id = api_key_obj.key
    now = datetime.utcnow()

    # Enterprise has no limit
    if plan == "enterprise":
        return

    # Get plan limit
    limit = API_PLANS.get(plan, 100)

    # If not yet tracked, initialize
    if key_id not in rate_limit_cache:
        rate_limit_cache[key_id] = {
            "count": 1,
            "reset": now + timedelta(days=1)
        }
        return

    record = rate_limit_cache[key_id]

    # Reset counter after 24h
    if now >= record["reset"]:
        rate_limit_cache[key_id] = {
            "count": 1,
            "reset": now + timedelta(days=1)
        }
        return

    # Check if limit is reached
    if record["count"] >= limit:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded for plan '{plan}'. Please upgrade or wait until reset."
        )

    # Otherwise, increment usage
    record["count"] += 1
