# AutoSuggestionEngine — Intelligent Recommendation System for SmartInjectGPT Owner

import random
from datetime import datetime
from typing import List, Dict

class AutoSuggestionEngine:
    def __init__(self):
        self.suggestions: List[Dict] = []

    def generate_suggestion(self, discovered_topic: str, risk_score: float) -> Dict:
        idea_bank = {
            "Autonomous AI Agent": "SmartCollabBot — a self-managing assistant for business owners.",
            "Quantum Technology": "SmartSecureLedger — encrypted blockchain accounting built on quantum-proof keys.",
            "Neural Interface": "NeuroConnectBot — mind-to-message assistant for SmartBiz customers.",
            "General Innovation": "SmartMarketBot — AI for real-time trend analysis and offer predictions."
        }

        idea = idea_bank.get(discovered_topic, "SmartVisionX — explore and propose future-proof modules.")
        suggestion = {
            "timestamp": datetime.utcnow().isoformat(),
            "topic": discovered_topic,
            "risk_score": risk_score,
            "idea": idea,
            "status": "PENDING_OWNER_DECISION"
        }
        self.suggestions.append(suggestion)
        return suggestion

    def list_pending_suggestions(self) -> List[Dict]:
        return [s for s in self.suggestions if s["status"] == "PENDING_OWNER_DECISION"]

    def update_decision(self, index: int, decision: str):
        if index >= len(self.suggestions):
            return {"error": "Invalid index"}
        if decision not in ["approve", "delay", "dismiss"]:
            return {"error": "Invalid decision type"}

        self.suggestions[index]["status"] = decision.upper()
        self.suggestions[index]["decision_time"] = datetime.utcnow().isoformat()
        return self.suggestions[index]
