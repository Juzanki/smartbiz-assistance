# vision_engine.py — Strategic Planner AI for Future Feature Roadmap

from datetime import datetime
from typing import Dict, List

class VisionEngine:
    def __init__(self):
        self.vision_log: List[Dict] = []
        self.future_features: List[Dict] = []
        self.tech_trends: List[str] = []

    def submit_vision(self, idea: str, target_date: str, category: str = "feature") -> Dict:
        plan = {
            "idea": idea,
            "target_date": target_date,
            "category": category,
            "created_at": datetime.utcnow().isoformat()
        }
        self.vision_log.append(plan)

        if category == "feature":
            self.future_features.append(plan)

        return {
            "status": "accepted",
            "entry": plan
        }

    def get_roadmap(self, year: int = None) -> List[Dict]:
        return [
            item for item in self.vision_log
            if not year or str(year) in item["target_date"]
        ]

    def add_tech_trend(self, topic: str):
        if topic not in self.tech_trends:
            self.tech_trends.append(topic)

    def get_trends(self) -> List[str]:
        return self.tech_trends[-5:]

    def suggest_next_features(self) -> List[str]:
        suggestions = []
        if "blockchain integration" in self.tech_trends:
            suggestions.append("Add SmartContract support to payment modules.")
        if "real-time AI analytics" in self.tech_trends:
            suggestions.append("Integrate live dashboards with auto-analysis.")
        if not suggestions:
            suggestions.append("No trend-based suggestions found.")
        return suggestions
