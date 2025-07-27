# ProgressTracker — Monitors Feature Building Progress for SmartCreatorAI

from datetime import datetime
from typing import Dict, List

class ProgressTracker:
    def __init__(self):
        self.feature_logs: Dict[str, List[Dict]] = {}

    def start_feature(self, feature_name: str):
        self.feature_logs[feature_name] = []
        self.log(feature_name, "🔧 Started building feature.")

    def log(self, feature_name: str, message: str, percent: int = None):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": message
        }
        if percent is not None:
            entry["progress"] = percent
        self.feature_logs.setdefault(feature_name, []).append(entry)

    def update_progress(self, feature_name: str, stage: str, percent: int):
        msg = f"⏳ Progress at {stage}: {percent}%"
        self.log(feature_name, msg, percent)

    def complete_feature(self, feature_name: str):
        self.log(feature_name, "✅ Feature completed.", 100)

    def get_status(self, feature_name: str) -> Dict:
        logs = self.feature_logs.get(feature_name, [])
        latest = logs[-1] if logs else {}
        percent = latest.get("progress", 0)
        return {
            "feature": feature_name,
            "progress": percent,
            "latest_update": latest.get("message", "Not started"),
            "entries": logs
        }
