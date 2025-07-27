# SecretCommander — AI Authority Validation Layer for SmartInjectGPT

import hashlib
from datetime import datetime, timedelta

class SecretCommander:
    def __init__(self, owner_signature: str, allowed_window_minutes: int = 3):
        self.owner_signature_hash = owner_signature
        self.active_window = None
        self.allowed_window = allowed_window_minutes

    def _hash_signature(self, key: str) -> str:
        return hashlib.sha256(key.encode()).hexdigest()

    def authenticate_owner(self, signature: str) -> bool:
        if self._hash_signature(signature) == self.owner_signature_hash:
            self.active_window = {
                "start": datetime.utcnow(),
                "end": datetime.utcnow() + timedelta(minutes=self.allowed_window)
            }
            print(f"[AUTH] Owner verified. Access active until {self.active_window['end'].isoformat()}")
            return True
        print("[AUTH] Invalid signature. Access denied.")
        return False

    def has_authority(self) -> bool:
        if not self.active_window:
            return False
        now = datetime.utcnow()
        return self.active_window["start"] <= now <= self.active_window["end"]

    def execute_command(self, command: str) -> str:
        if not self.has_authority():
            return "[DENIED] No valid spiritual authorization window."

        if command == "shutdown_kernel":
            return "[EXECUTED] Kernel shutdown signal issued."
        elif command == "inject_code_silently":
            return "[EXECUTED] Silent injection authorized."
        elif command == "rebuild_AI":
            return "[EXECUTED] Strategic rebuild of SmartInjectGPT initiated."
        else:
            return "[REJECTED] Unknown or unlisted command."
