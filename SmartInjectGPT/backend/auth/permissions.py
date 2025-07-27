# backend/auth/permissions.py

import json
import logging
from pathlib import Path

PERMISSIONS_FILE = Path(__file__).parent / "permissions.json"

def load_permissions():
    """
    Load permissions configuration from permissions.json.
    Returns a dictionary of permissions.
    """
    if not PERMISSIONS_FILE.exists():
        logging.warning("⚠️ Permissions file not found at expected location.")
        return {}

    try:
        with open(PERMISSIONS_FILE, "r", encoding="utf-8") as f:
            permissions = json.load(f)
            logging.info("✅ Permissions loaded.")
            return permissions
    except json.JSONDecodeError as e:
        logging.error(f"❌ Invalid JSON format in permissions file: {e}")
        return {}
    except Exception as e:
        logging.error(f"❌ Unexpected error reading permissions: {e}")
        return {}

# Test only when run directly
if __name__ == "__main__":
    print(load_permissions())
