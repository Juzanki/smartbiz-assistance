# DivineSignature — Multi-Layer Spiritual Identity Verification for SmartInjectGPT

import hashlib
from datetime import datetime
import logging
import os

class DivineSignature:
    def __init__(self, expected_signature_hash: str):
        self.expected_signature_hash = expected_signature_hash
        self.last_verified = None
        self.secret_phrase = "SmartInjectGPT-DIVINE-TRUTH"

    def generate_signature(self, device_id: str, typing_pattern: str, access_time: str, secret_phrase: str) -> str:
        combined = f"{device_id}|{typing_pattern}|{access_time}|{secret_phrase}"
        return hashlib.sha256(combined.encode()).hexdigest()

    def verify_signature(
        self,
        device_id: str,
        typing_pattern: str,
        access_time: str,
        secret_phrase: str
    ) -> bool:
        generated = self.generate_signature(device_id, typing_pattern, access_time, secret_phrase)
        if generated == self.expected_signature_hash:
            self.last_verified = datetime.utcnow().isoformat()
            logging.info("[DIVINE] ✅ Multi-layer signature verified.")
            return True
        logging.warning("[DIVINE] ❌ Multi-layer signature mismatch.")
        return False

    def verify(self) -> bool:
        """
        Basic verification fallback using only the fixed phrase.
        Used by kernel at startup (minimal context).
        """
        hashed = hashlib.sha256(self.secret_phrase.encode()).hexdigest()
        if hashed == self.expected_signature_hash:
            self.last_verified = datetime.utcnow().isoformat()
            logging.info("[DIVINE] ✅ Basic divine signature verified.")
            return True
        logging.error("[DIVINE] ❌ Basic divine signature mismatch.")
        return False

    def get_last_verified(self):
        return self.last_verified
