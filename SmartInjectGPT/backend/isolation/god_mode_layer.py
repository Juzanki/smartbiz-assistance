# GodModeLayer — Ephemeral Access Control for Core AI Kernel

import os
from datetime import datetime, timedelta
import hashlib

class GodModeLayer:
    def __init__(self, spiritual_key_hash: str, window_minutes: int = 3):
        self._spiritual_key_hash = spiritual_key_hash
        self._access_window = None
        self._window_minutes = window_minutes

    def _hash_key(self, key: str) -> str:
        return hashlib.sha256(key.encode()).hexdigest()

    def authorize(self, key: str) -> bool:
        if self._hash_key(key) != self._spiritual_key_hash:
            print("[GODMODE] Invalid spiritual key.")
            return False
        self._access_window = {
            "start": datetime.utcnow(),
            "end": datetime.utcnow() + timedelta(minutes=self._window_minutes)
        }
        print(f"[GODMODE] Access granted until {self._access_window['end'].isoformat()}")
        return True

    def is_access_open(self) -> bool:
        if not self._access_window:
            return False
        now = datetime.utcnow()
        return self._access_window["start"] <= now <= self._access_window["end"]

    def access_core_ai(self):
        if self.is_access_open():
            print("[GODMODE] Core AI Kernel access granted.")
            return True
        else:
            print("[GODMODE] Access denied. Time window closed.")
            return False
