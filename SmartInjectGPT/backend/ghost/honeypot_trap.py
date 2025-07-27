# HoneypotTrap — Deceptive Sandbox Zone for Intruder Containment

import random
from datetime import datetime

class HoneypotTrap:
    def __init__(self):
        self.trap_active = False
        self.trap_logs = []

    def activate_trap(self, ip: str, user_agent: str):
        self.trap_active = True
        self.trap_logs.append({
            "timestamp": datetime.utcnow().isoformat(),
            "ip": ip,
            "user_agent": user_agent,
            "action": "TRAP ACTIVATED"
        })

    def get_fake_dashboard(self) -> dict:
        if not self.trap_active:
            return {"error": "Trap not active."}
        return {
            "status": "ok",
            "user": "admin",
            "last_login": "March 2019",
            "data": [random.randint(1000, 9999) for _ in range(3)],
            "features": ["Upload", "Download", "Run Job"],
            "note": "All systems appear functional."
        }

    def fake_injection_response(self, command: str) -> str:
        if not self.trap_active:
            return "Command rejected."
        return f"Command '{command}' accepted and scheduled. [FAKE_EXECUTION]"

    def get_trap_logs(self, limit: int = 5):
        return self.trap_logs[-limit:]

    def deactivate_trap(self):
        self.trap_active = False
