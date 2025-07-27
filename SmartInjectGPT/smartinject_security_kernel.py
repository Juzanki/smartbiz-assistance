# SmartInject Security Kernel — AI Zero-Trust Core for Self-Defense & Threat Response

from SmartInjectGPT.defense.defense_core import DefenseCore
from SmartInjectGPT.defense.counterintel_agent import CounterIntelAgent
from SmartInjectGPT.ghost.ghost_core import GhostCore
from SmartInjectGPT.intelligence.ai_defense_core import AIDefenseCore

class SmartInjectSecurityKernel:
    def __init__(self, owner_hash: str, safe_ips: list):
        self.ghost = GhostCore(owner_hash=owner_hash, safe_ips=safe_ips)
        self.defender = DefenseCore()
        self.intel = AIDefenseCore()
        self.counterintel = CounterIntelAgent()

    def process_request(self, request: dict) -> dict:
        text = request.get("input", "")
        ip = request.get("ip", "unknown")
        user_agent = request.get("user_agent", "unknown")
        device = request.get("device", "unknown")
        typing = request.get("typing_pattern", "")
        access_time = request.get("access_time", "")
        secret_phrase = request.get("secret_phrase", "")

        # === Step 1: Threat Analysis (Prompt + Fingerprint + Global Intelligence) ===
        threat = self.intel.process_input(text, ip)
        alerts = []

        if threat["detected"]:
            self.counterintel.log_attempt(ip, user_agent, vector=text, fingerprint="auto-match")
            alerts.append(threat["reason"])

        # === Step 2: Virus Payload Scanner ===
        virus = self.defender.inspect_input(text)
        if virus["infected"]:
            alerts.append("Malicious payload detected. Shield locked.")

        # === Step 3: Divine Signature + Travel Check ===
        access_status = self.ghost.handle_request(ip, user_agent, device, typing, access_time, secret_phrase)

        # === Final Response ===
        return {
            "status": "shielded" if self.defender.shield.is_locked() else "allowed",
            "ghost_mode": self.ghost.get_status(),
            "threat_report": threat,
            "virus_report": virus,
            "access_decision": access_status,
            "counterintel_alerts": self.counterintel.get_recent_alerts(),
            "global_alerts": self.intel.scan_global_threats()[:2],
            "summary": alerts
        }
