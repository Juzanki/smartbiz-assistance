# GhostGuardian — Deceptive Shield Mode for SmartInjectGPT

import random
from datetime import datetime

class GhostGuardian:
    def __init__(self):
        self.fake_data_enabled = False
        self.silent_mode = False
        self.log = []

    def activate_fake_data(self):
        self.fake_data_enabled = True
        self._log("Fake Data Mode ON")

    def activate_silent_mode(self):
        self.silent_mode = True
        self._log("Silent Null Response Mode ON")

    def _log(self, message: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": message
        }
        self.log.append(entry)

    def get_data(self, query: str) -> dict:
        if self.fake_data_enabled:
            return self._generate_fake_response(query)
        if self.silent_mode:
            return {}
        return {"error": "GhostGuardian not activated."}

    def _generate_fake_response(self, query: str) -> dict:
        samples = [
            {"username": "admin", "password": "123456", "role": "user"},
            {"email": "test@example.com", "token": "xyz123", "status": "active"},
            {"message": "Welcome to SmartInjectGPT", "plan": "Free"}
        ]
        fake = random.choice(samples)
        self._log(f"Returned fake response for query '{query}'")
        return fake

    def block_execution(self) -> bool:
        return self.silent_mode or self.fake_data_enabled

    def get_logs(self):
        return self.log[-5:]
