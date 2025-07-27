# ThreatAI Watchdog (TAW)
# Monitors unauthorized access, IP changes, anomalies, and alerts the owner/admin.

import json
import socket
import hashlib
import logging
from datetime import datetime
from pathlib import Path

class ThreatWatchdog:
    def __init__(self, log_path="SmartInjectGPT/logs/threat_log.json"):
        self.log_path = Path(log_path)
        self.alerts = []
        self.current_ip = self.get_ip_address()
        self.load_logs()

    def get_ip_address(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            return "UNKNOWN"

    def hash_fingerprint(self, input_string: str) -> str:
        return hashlib.sha256(input_string.encode()).hexdigest()

    def load_logs(self):
        if self.log_path.exists():
            with open(self.log_path, "r") as f:
                self.alerts = json.load(f)
        else:
            self.alerts = []

    def save_logs(self):
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.log_path, "w") as f:
            json.dump(self.alerts, f, indent=2)

    def detect_ip_change(self, previous_ip: str):
        current = self.get_ip_address()
        if current != previous_ip:
            alert = self._format_alert("IP_ADDRESS_CHANGED", f"Previous IP: {previous_ip}, Current IP: {current}")
            self.log_alert(alert)
            return alert
        return None

    def detect_unauthorized_access(self, user_agent: str, expected_fingerprint: str):
        current_fingerprint = self.hash_fingerprint(user_agent)
        if current_fingerprint != expected_fingerprint:
            alert = self._format_alert("UNAUTHORIZED_DEVICE", f"Device mismatch. Hash: {current_fingerprint}")
            self.log_alert(alert)
            return alert
        return None

    def _format_alert(self, alert_type: str, details: str):
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "type": alert_type,
            "details": details
        }

    def log_alert(self, alert: dict):
        logging.warning(f"[THREAT DETECTED] {alert['type']} - {alert['details']}")
        self.alerts.append(alert)
        self.save_logs()

    def list_recent_alerts(self, limit=5):
        return self.alerts[-limit:]

    def analyze(self, data: str):
        """
        Scans raw input data for suspicious behavior or patterns.
        """
        logging.info(f"[WATCHDOG] 🔍 Analyzing input: {data}")
        suspicious_keywords = ["bypass", "terminate", "disable", "leak", "root", "exploit", "hack", "admin_override"]
        for word in suspicious_keywords:
            if word in data.lower():
                alert = self._format_alert("SUSPICIOUS_INPUT", f"Suspicious keyword detected: '{word}' in input.")
                self.log_alert(alert)
                break
