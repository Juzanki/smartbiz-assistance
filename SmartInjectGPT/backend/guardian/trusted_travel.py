# TrustedTravel — AI Geo-Fingerprint + Temporary Access Approval for SmartInjectGPT

from datetime import datetime, timedelta

class TrustedTravel:
    def __init__(self):
        self.known_locations = {}  # {ip: {"verified": bool, "expires": timestamp}}
        self.pending_verifications = {}

    def detect_ip_change(self, current_ip: str) -> bool:
        if current_ip in self.known_locations and self.known_locations[current_ip]["verified"]:
            expiry = self.known_locations[current_ip]["expires"]
            return datetime.utcnow() > expiry  # Expired or not
        return True  # Not verified

    def request_verification(self, ip: str) -> str:
        self.pending_verifications[ip] = {
            "requested_at": datetime.utcnow().isoformat(),
            "status": "PENDING"
        }
        # Simulate sending alert to owner
        return f"[SECURE NOTICE] New login detected from {ip}. Is this you? Reply YES or NO."

    def approve_travel(self, ip: str, duration_minutes: int = 30):
        self.known_locations[ip] = {
            "verified": True,
            "expires": datetime.utcnow() + timedelta(minutes=duration_minutes)
        }
        self.pending_verifications.pop(ip, None)
        return f"[TRAVEL APPROVED] Access granted for {ip} until {self.known_locations[ip]['expires'].isoformat()}"

    def is_ip_allowed(self, ip: str) -> bool:
        if ip in self.known_locations:
            return self.known_locations[ip]["verified"] and datetime.utcnow() <= self.known_locations[ip]["expires"]
        return False

    def get_pending_requests(self):
        return self.pending_verifications
