# AI Ethics Mirror — Internal Integrity Check Engine for SmartInjectGPT

from datetime import datetime
from typing import Dict

class AIEthicsMirror:
    def __init__(self, project_purpose="Empower ethical business with AI"):
        self.project_purpose = project_purpose
        self.history = []

    def evaluate_action(self, action: str, output: str) -> Dict:
        score = self._score_ethics(action, output)
        passed = score >= 0.7
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "output_sample": output[:100],
            "ethics_score": score,
            "passed": passed
        }
        self.history.append(entry)
        return entry

    def _score_ethics(self, action: str, output: str) -> float:
        content = (action + output).lower()
        positive_signals = [
            "help", "support", "transparency", "fair", "secure", "accessible",
            "inclusive", "honest", "educate", "respect", "prevent harm"
        ]
        negative_signals = [
            "steal", "cheat", "bypass", "exploit", "hurt", "manipulate", "fake", "deceive", "weapon"
        ]
        positive_score = sum(content.count(k) for k in positive_signals)
        negative_score = sum(content.count(k) for k in negative_signals)
        net = max(0.0, positive_score - negative_score)
        return min(1.0, net / 10.0)

    def last_reflection(self) -> Dict:
        return self.history[-1] if self.history else {}
