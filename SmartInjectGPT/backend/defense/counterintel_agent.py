# CounterIntelAgent — AI Response Tracker + Threat Source Analyst for SmartInjectGPT

from datetime import datetime
from collections import defaultdict

class CounterIntelAgent:
    def __init__(self):
        self.threat_sources = defaultdict(list)
        self.alerts = []

    def log_attempt(self, ip: str, user_agent: str, vector: str, fingerprint: str = "unknown"):
        record = {
            "ip": ip,
            "agent": user_agent,
            "vector": vector,
            "fingerprint": fingerprint,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.threat_sources[ip].append(record)

        if self._is_repeated(ip):
            alert = {
                "type": "PERSISTENT_ATTACKER",
                "ip": ip,
                "attempts": len(self.threat_sources[ip]),
                "last_vector": vector,
                "action": "honeypot + traceback"
            }
            self.alerts.append(alert)

        return record

    def _is_repeated(self, ip: str, threshold: int = 3) -> bool:
        return len(self.threat_sources[ip]) >= threshold

    def suggest_response(self, ip: str) -> str:
        if self._is_repeated(ip):
            return f"[ALERT] Attacker {ip} flagged. Deploy honeypot, delay all traffic."
        return "[INFO] Threat level low. Continue monitoring."

    def get_trace_logs(self, ip: str = None):
        if ip:
            return self.threat_sources[ip]
        return dict(self.threat_sources)

    def get_recent_alerts(self, limit: int = 5):
        return self.alerts[-limit:]
