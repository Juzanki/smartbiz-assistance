# threat_ai_core.py — Detects External AI, Malicious Payloads, and Unauthorized Access

import re
from datetime import datetime
from typing import Dict, List

class ThreatAICore:
    def __init__(self):
        self.threat_signatures = [
            "eval\\(", "exec\\(", "subprocess", "base64_decode", "os\\.system",
            "AgentGPT", "AutoGPT", "Langchain Probe", "payload injection",
            "traceback spoof", "AI Signature Mismatch", "GPT-Stealer"
        ]
        self.suspicious_ips = []
        self.detections: List[Dict] = []

    def scan_code_or_payload(self, text: str, source_ip: str = "unknown") -> Dict:
        matches = []
        for pattern in self.threat_signatures:
            if re.search(pattern, text, re.IGNORECASE):
                matches.append(pattern)

        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "source": source_ip,
            "threat_detected": bool(matches),
            "matched_patterns": matches,
            "action": None
        }

        if matches:
            self.suspicious_ips.append(source_ip)
            result["action"] = "🔒 Lockdown or GhostMode suggested"
            self.detections.append(result)

        return result

    def get_all_threat_logs(self, limit=5) -> List[Dict]:
        return self.detections[-limit:]

    def is_ip_flagged(self, ip: str) -> bool:
        return ip in self.suspicious_ips
