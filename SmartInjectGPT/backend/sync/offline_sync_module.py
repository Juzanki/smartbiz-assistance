# offline_sync_module.py — AI-Driven Offline Cache + Auto Sync System

import os
import json
from datetime import datetime
from typing import List, Dict

class OfflineSyncModule:
    def __init__(self, cache_path: str = "SmartInjectGPT/sync/cache.json"):
        self.cache_path = cache_path
        self.synced_log: List[Dict] = []

        # Ensure cache file exists
        if not os.path.exists(cache_path):
            with open(cache_path, "w") as f:
                json.dump([], f)

    def save_to_cache(self, payload: Dict):
        payload["timestamp"] = datetime.utcnow().isoformat()
        with open(self.cache_path, "r") as f:
            data = json.load(f)

        data.append(payload)

        with open(self.cache_path, "w") as f:
            json.dump(data, f, indent=4)

        return f"✅ Payload cached offline. Total: {len(data)}"

    def is_online(self) -> bool:
        try:
            import requests
            requests.get("https://www.google.com", timeout=3)
            return True
        except:
            return False

    def sync_all(self) -> Dict:
        if not self.is_online():
            return {"status": "offline", "message": "Still no internet connection."}

        with open(self.cache_path, "r") as f:
            cached_data = json.load(f)

        synced = []
        for item in cached_data:
            # Future: send this to a real backend
            self.synced_log.append(item)
            synced.append(item)

        # Clear cache after sync
        with open(self.cache_path, "w") as f:
            json.dump([], f)

        return {
            "status": "online",
            "synced_items": len(synced),
            "last_synced": datetime.utcnow().isoformat()
        }

    def get_synced_history(self, limit=5):
        return self.synced_log[-limit:]
