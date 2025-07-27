# DefenseCore — Central AI Security Manager for SmartInjectGPT

from SmartInjectGPT.defense.ai_self_shield import AISelfShield
from SmartInjectGPT.defense.virus_guardian import VirusGuardian
from datetime import datetime

class DefenseCore:
    def __init__(self):
        self.shield = AISelfShield()
        self.virus_guard = VirusGuardian()
        self.last_action = None

    def inspect_input(self, user_input: str) -> dict:
        scan = self.virus_guard.scan(user_input)
        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "infected": scan["infected"],
            "threat_patterns": scan["matches"],
            "action": "allow"
        }

        if scan["infected"]:
            self.shield.engage_lockdown("Virus/payload pattern detected.")
            result["action"] = "lockdown"
        else:
            if self.shield.is_locked():
                result["action"] = "blocked_by_shield"

        self.last_action = result
        return result

    def override_lock(self, token: str) -> str:
        return self.shield.release_lockdown(owner_override=token)

    def get_status(self) -> dict:
        return {
            "shield_status": self.shield.status(),
            "last_threat_response": self.last_action
        }
