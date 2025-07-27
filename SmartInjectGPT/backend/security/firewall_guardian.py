# FirewallGuardian — Protects SmartInjectGPT Kernel from Suspicious or Unauthorized Access

import logging
from datetime import datetime
from typing import List, Dict


class FirewallGuardian:
    def __init__(self, safe_ips: List[str], alert_callback=None):
        self.safe_ips = safe_ips
        self.alert_callback = alert_callback
        self.threat_log: List[Dict] = []
        self.silent_mode = False

    def log_threat(self, ip: str, reason: str):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "ip": ip,
            "reason": reason
        }
        self.threat_log.append(log_entry)
        logging.warning(f"[FIREWALL] Threat from {ip} — {reason}")
        if self.alert_callback:
            self.alert_callback(f"Unauthorized access from {ip}: {reason}")
        self.silent_mode = True

    def is_safe(self, ip: str) -> bool:
        if ip in self.safe_ips:
            return True
        self.log_threat(ip, "IP not in allowlist")
        return False

    def block_injection(self, ip: str) -> bool:
        if not self.is_safe(ip):
            return True  # block it
        if self.silent_mode:
            logging.warning("[FIREWALL] Silent mode active — all injections blocked.")
            return True
        return False

    def reset_silent_mode(self):
        self.silent_mode = False
        logging.info("[FIREWALL] Silent mode cleared.")

    # ✅ New method to scan text input for suspicious patterns
    def scan(self, input_data: str):
        logging.info(f"[FIREWALL] 🔍 Scanning input data: {input_data}")
        flagged_words = ["hack", "breach", "exploit", "inject", "override", "steal", "token", "shutdown"]
        for word in flagged_words:
            if word in input_data.lower():
                self.log_threat(ip="N/A", reason=f"Suspicious keyword detected: '{word}'")
                break
