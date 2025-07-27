# AIDefenseCore — Unified Threat Detection Engine for SmartInjectGPT

from SmartInjectGPT.intelligence.threat_analyzer_bot import ThreatAnalyzerBot
from SmartInjectGPT.intelligence.ai_fingerprint_db import AIFingerprintDB
from SmartInjectGPT.intelligence.darknet_awareness import DarknetAwareness

class AIDefenseCore:
    def __init__(self):
        self.analyzer = ThreatAnalyzerBot()
        self.fingerprint_db = AIFingerprintDB()
        self.darknet = DarknetAwareness()
        self.last_analysis = {}

    def process_input(self, text: str, ip: str = "unknown") -> dict:
        # Step 1: Analyze prompt pattern
        base_result = self.analyzer.analyze_input(text, ip=ip)

        # Step 2: Check for known AI fingerprints
        fingerprints = self.fingerprint_db.check_against_fingerprints(text)
        if fingerprints:
            base_result["fingerprints"] = fingerprints
            base_result["action"] = "block + log"
            base_result["reason"] += f" | Fingerprint match: {', '.join(fingerprints)}"
            base_result["detected"] = True
            base_result["score"] = max(base_result["score"], 0.9)

        self.last_analysis = base_result
        return base_result

    def scan_global_threats(self):
        return self.darknet.scan_all()

    def get_recent_alerts(self):
        return {
            "prompt_threats": self.analyzer.get_recent_threats(),
            "darknet_feeds": self.darknet.get_last_alerts()
        }

    def last_decision(self):
        return self.last_analysis
