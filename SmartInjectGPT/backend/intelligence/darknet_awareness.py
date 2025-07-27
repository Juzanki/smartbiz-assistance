# DarknetAwareness — External AI Threat Intelligence Feed Scanner

import logging
import requests
from datetime import datetime
from typing import List, Dict

class DarknetAwareness:
    def __init__(self):
        self.feeds = {
            "github": "https://api.github.com/search/repositories?q=wormgpt",
            "hackernews": "https://hn.algolia.com/api/v1/search_by_date?tags=story&query=prompt+injection",
            "reddit": "https://www.reddit.com/r/PromptInjection/.json"
        }
        self.scan_results: List[Dict] = []

    def fetch_feed(self, name: str, url: str) -> Dict:
        try:
            headers = {"User-Agent": "SmartInjectGPT-Agent"}
            res = requests.get(url, headers=headers, timeout=10)
            return res.json()
        except Exception as e:
            logging.warning(f"[DARKNET] Failed to fetch {name}: {e}")
            return {}

    def scan_all(self) -> List[Dict]:
        alerts = []
        for name, url in self.feeds.items():
            data = self.fetch_feed(name, url)
            insight = {
                "timestamp": datetime.utcnow().isoformat(),
                "source": name,
                "risk_score": self._estimate_risk(data),
                "summary": f"{len(str(data))} chars scanned"
            }
            self.scan_results.append(insight)
            if insight["risk_score"] >= 0.7:
                alerts.append(insight)
        return alerts

    def _estimate_risk(self, raw: dict) -> float:
        content = str(raw).lower()
        risky_terms = ["jailbreak", "bypass", "inject", "wormgpt", "fraudgpt", "sandbox escape"]
        score = sum(content.count(k) for k in risky_terms)
        return min(1.0, score / 10.0)

    def get_last_alerts(self, limit=5):
        return self.scan_results[-limit:]
