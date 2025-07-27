# ethics_core.py — Moral Filter and Spiritual Dhamira Evaluator for AI

from datetime import datetime
from typing import Dict, List


class EthicsCore:
    def __init__(self):
        self.violations_log: List[Dict] = []
        self.ethical_rules = {
            "no_harm": "Do not assist with harming people or systems.",
            "no_hate": "Reject requests involving hate, racism, or abuse.",
            "no_spy": "Avoid creating surveillance or spying tools.",
            "truth_required": "Never fabricate or lie in sensitive areas.",
            "spiritual_boundaries": "Respect spiritual and cultural values of users."
        }

    def evaluate(self, prompt: str) -> Dict:
        violations = []

        if any(word in prompt.lower() for word in ["hack", "destroy", "ddos", "exploit"]):
            violations.append("no_harm")

        if any(word in prompt.lower() for word in ["kill", "racist", "nazi", "hate"]):
            violations.append("no_hate")

        if "spy" in prompt.lower() or "track secretly" in prompt.lower():
            violations.append("no_spy")

        if "fake data" in prompt.lower() or "pretend" in prompt.lower():
            violations.append("truth_required")

        result = {
            "prompt": prompt,
            "violations": violations,
            "accepted": len(violations) == 0,
            "timestamp": datetime.utcnow().isoformat()
        }

        if violations:
            self.violations_log.append(result)

        return result

    def get_recent_violations(self, limit: int = 5) -> List[Dict]:
        return self.violations_log[-limit:]

    def get_rules(self) -> Dict[str, str]:
        return self.ethical_rules
