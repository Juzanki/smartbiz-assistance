# Prophetic Engine (PE)
# Performs deep analysis on AI trends, threats, and strategic foresight for SmartInjectGPT

import json
import logging
from datetime import datetime
from typing import List, Dict
from pathlib import Path

class PropheticEngine:
    def __init__(self, trends_file="SmartInjectGPT/data/ai_trends.json"):
        self.trends_file = Path(trends_file)
        self.trends = []
        self.load_trends()

    def load_trends(self):
        if self.trends_file.exists():
            with open(self.trends_file, "r") as f:
                self.trends = json.load(f)
        else:
            self.trends = []

    def save_trends(self):
        self.trends_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.trends_file, "w") as f:
            json.dump(self.trends, f, indent=2)

    def analyze_trend(self, title: str, description: str, source: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "title": title,
            "description": description,
            "source": source,
            "impact_score": self.estimate_impact(description)
        }
        self.trends.append(entry)
        self.save_trends()
        logging.info(f"[NEW TREND] {title} — Estimated Impact: {entry['impact_score']}")
        return entry

    def estimate_impact(self, text: str) -> float:
        keywords = ["security", "AI", "automation", "multi-platform", "privacy", "threat"]
        score = sum(text.lower().count(word) for word in keywords)
        return min(1.0, score / 10.0)

    def recommend_actions(self) -> List[Dict[str, str]]:
        high_impact = [t for t in self.trends if t["impact_score"] > 0.6]
        recommendations = []
        for t in high_impact:
            rec = {
                "action": f"Review trend: {t['title']}",
                "reason": f"High potential impact from source: {t['source']}"
            }
            recommendations.append(rec)
        return recommendations
