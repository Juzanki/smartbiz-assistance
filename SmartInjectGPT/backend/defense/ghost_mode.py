# ghost_mode.py — AI Cloaking, Distraction, and Silent Lockdown System

from datetime import datetime
from typing import List, Dict


class GhostModeAI:
    def __init__(self):
        self.state = "visible"
        self.fake_responses: List[Dict] = []
        self.incidents: List[Dict] = []

    def activate_ghost_mode(self, reason: str) -> Dict:
        self.state = "ghost"
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "mode": "GHOST",
            "trigger_reason": reason
        }
        self.incidents.append(entry)
        return {
            "status": "🔒 Ghost Mode Activated",
            "details": entry
        }

    def deactivate(self) -> str:
        self.state = "visible"
        return "🟢 Ghost Mode Deactivated. System restored."

    def is_active(self) -> bool:
        return self.state == "ghost"

    def fake_data_response(self, request_type: str) -> Dict:
        fake = {
            "request": request_type,
            "data": "This is a dummy response for obfuscation purposes.",
            "timestamp": datetime.utcnow().isoformat()
        }
        self.fake_responses.append(fake)
        return fake

    def lockdown(self) -> Dict:
        self.state = "lockdown"
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "mode": "LOCKDOWN",
            "action": "All external traffic disabled. Awaiting owner unlock."
        }
        self.incidents.append(entry)
        return {
            "status": "🛡️ Silent Lockdown Mode Initiated",
            "details": entry
        }

    def get_log(self, limit: int = 5) -> List[Dict]:
        return self.incidents[-limit:]
