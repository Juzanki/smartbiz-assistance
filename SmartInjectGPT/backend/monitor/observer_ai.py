# observer_ai.py — Monitors Main AI Behavior and Generates Monthly Reports

from datetime import datetime
from typing import List, Dict

class ObserverAI:
    def __init__(self):
        self.activity_log: List[Dict] = []
        self.monthly_reports: List[Dict] = []

    def log_activity(self, module: str, action: str, status: str = "success"):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": module,
            "action": action,
            "status": status
        }
        self.activity_log.append(log_entry)
        return log_entry

    def generate_monthly_report(self) -> Dict:
        count = len(self.activity_log)
        errors = [log for log in self.activity_log if log["status"] != "success"]

        report = {
            "month": datetime.utcnow().strftime("%Y-%m"),
            "total_actions": count,
            "errors_detected": len(errors),
            "error_details": errors[-5:],
            "timestamp": datetime.utcnow().isoformat()
        }
        self.monthly_reports.append(report)
        return report

    def get_recent_logs(self, limit: int = 5) -> List[Dict]:
        return self.activity_log[-limit:]

    def get_monthly_history(self) -> List[Dict]:
        return self.monthly_reports
