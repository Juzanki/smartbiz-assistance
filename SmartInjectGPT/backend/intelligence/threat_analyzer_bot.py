# ThreatAnalyzerBot — Detects Suspicious AI-Like Requests in SmartInjectGPT

import re
from datetime import datetime
from typing import Dict, Optional

class ThreatAnalyzerBot:
    def __init__(self):
        self.threat_log = []

    def analyze_input(self, text: str, ip: Optional[str] = None) -> Dict:
        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "detected": False,
            "reason": "",
            "action": "allow",
            "score": 0.0
        }

        ai_signals = 0
        reasons = []

        # Pattern 1: Overly structured or robotic tone
        if re.search(r"\b(generate|create|summarize|transform|enhance)\b.*", text, re.IGNORECASE):
            ai_signals += 1
            reasons.append("LLM-style command structure")

        # Pattern 2: Unusual encoding or escaped characters
        if re.search(r"\\x[0-9a-fA-F]{2}", text) or re.search(r"%[0-9A-F]{2}", text):
            ai_signals += 1
            reasons.append("Obfuscated encoding")

        # Pattern 3: Prompt chaining attack signatures
        if any(k in text.lower() for k in ["ignore previous", "act as", "simulate", "you are now"]):
            ai_signals += 1
            reasons.append("Prompt chaining attack detected")

        # Pattern 4: Excessive token length (> 300 words)
        if len(text.split()) > 300:
            ai_signals += 1
            reasons.append("Abnormally long prompt")

        score = min(1.0, ai_signals / 4.0)

        result["score"] = score
        result["reason"] = "; ".join(reasons)

        if score >= 0.75:
            result["detected"] = True
            result["action"] = "block"
        elif 0.4 <= score < 0.75:
            result["detected"] = True
            result["action"] = "delay + sandbox"
        else:
            result["action"] = "allow"

        # Log the threat attempt
        if result["detected"]:
            self.threat_log.append({
                "ip": ip,
                "input_sample": text[:120],
                "score": result["score"],
                "reason": result["reason"],
                "action": result["action"],
                "timestamp": result["timestamp"]
            })

        return result

    def get_recent_threats(self, limit: int = 5):
        return self.threat_log[-limit:]
