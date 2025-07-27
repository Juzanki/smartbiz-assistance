# AISelfShield — AI Lockdown & Self-Defense Mechanism for SmartInjectGPT

from datetime import datetime

class AISelfShield:
    def __init__(self):
        self.locked = False
        self.lock_reason = ""
        self.lock_time = None

    def engage_lockdown(self, reason: str):
        self.locked = True
        self.lock_reason = reason
        self.lock_time = datetime.utcnow().isoformat()
        return f"[LOCKDOWN] AI Shield activated: {reason}"

    def release_lockdown(self, owner_override: str):
        if owner_override == "divine-override-token":
            self.locked = False
            return "[OVERRIDE] Shield released by owner."
        return "[DENIED] Invalid override."

    def is_locked(self) -> bool:
        return self.locked

    def status(self):
        return {
            "locked": self.locked,
            "reason": self.lock_reason,
            "engaged_at": self.lock_time
        }
