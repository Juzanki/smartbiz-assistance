# Prophetic Vision Engine (PVE) — Future Intelligence Monitor for SmartInjectGPT

import json
import logging
import requests
from datetime import datetime
from typing import List, Dict
from pathlib import Path

class VisionEngine:
    def __init__(self, data_path="SmartInjectGPT/data/prophetic_visions.json"):
        self.vision_path = Path(data_path)
        self.vision_log: List[Dict] = []
        self.sources = [
            "https://api.github.com/trending",
            "https://hn.algolia.com/api/v1/search_by_date?tags=story",
            # Add more sources as needed
        ]
        self._load_log()

    def _load_log(self):
        if self.vision_path.exists():
            self.vision_log = json.loads(self.vision_path.read_text())
        else:
            self.vision_log = []

    def _save_log(self):
        self.vision_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.vision_path, "w") as f:
            json.dump(self.vision_log, f, indent=2)

    def scan_sources(self):
        new_entries = []
        for url in self.sources:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    new_entries.append({
                        "source": url,
                        "data": response.json(),
                        "timestamp": datetime.utcnow().isoformat()
                    })
                    logging.info(f"[VISION] Scanned {url}")
                else:
                    logging.warning(f"[VISION] Failed to scan {url} — {response.status_code}")
            except Exception as e:
                logging.error(f"[VISION] Error scanning {url}: {e}")
        return new_entries

    def analyze_and_store(self, entries: List[Dict]):
        for entry in entries:
            insight = {
                "timestamp": datetime.utcnow().isoformat(),
                "source": entry["source"],
                "topic_detected": self._extract_topic(entry["data"]),
                "risk": self._estimate_risk(entry["data"]),
                "raw": entry["data"]
            }
            self.vision_log.append(insight)
        self._save_log()

    def _extract_topic(self, data: dict) -> str:
        try:
            content = json.dumps(data).lower()
            if "quantum" in content:
                return "Quantum Technology"
            elif "neuralink" in content:
                return "Neural Interface"
            elif "openai" in content and "agent" in content:
                return "Autonomous AI Agent"
            else:
                return "General Innovation"
        except:
            return "Unknown"

    def _estimate_risk(self, data: dict) -> float:
        content = json.dumps(data).lower()
        keywords = ["threat", "shutdown", "malicious", "agent", "blackbox"]
        return min(1.0, sum(content.count(k) for k in keywords) / 10.0)

    def report(self) -> List[Dict[str, str]]:
        return [{
            "topic": entry["topic_detected"],
            "source": entry["source"],
            "risk": entry["risk"]
        } for entry in self.vision_log[-5:]]
