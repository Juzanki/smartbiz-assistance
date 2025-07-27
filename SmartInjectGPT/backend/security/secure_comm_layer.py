# secure_comm_layer.py — Secure Internal Communication Bus for SmartInjectGPT Modules

import hashlib
import time
import json
from typing import Dict, Optional

class SecureCommLayer:
    def __init__(self, comm_log_file: str = "SmartInjectGPT/security/comm_log.json"):
        self.log_path = comm_log_file
        self.shared_key = "0xSMARTKEY-TRUTH-SECURE-CORE"
        self.module_registry = ["kernel", "builder", "patcher", "validator", "guardian", "prophecy", "observer", "memory"]
        self._init_log()

    def _init_log(self):
        try:
            with open(self.log_path, "x") as f:
                json.dump([], f)
        except FileExistsError:
            pass

    def _generate_signature(self, data: str) -> str:
        return hashlib.sha256((data + self.shared_key).encode()).hexdigest()

    def send(self, sender: str, receiver: str, payload: Dict) -> Dict:
        if sender not in self.module_registry or receiver not in self.module_registry:
            return {"status": "❌ Rejected", "reason": "Unregistered module"}

        message = {
            "timestamp": int(time.time()),
            "from": sender,
            "to": receiver,
            "payload": payload,
            "signature": self._generate_signature(json.dumps(payload, sort_keys=True))
        }

        with open(self.log_path, "r+") as f:
            history = json.load(f)
            history.append(message)
            f.seek(0)
            json.dump(history, f, indent=2)

        return {
            "status": "✅ Delivered",
            "to": receiver,
            "verified": True,
            "signature": message["signature"]
        }

    def verify(self, payload: Dict, signature: str) -> bool:
        expected = self._generate_signature(json.dumps(payload, sort_keys=True))
        return expected == signature

    def recent_communications(self, limit: int = 5) -> Optional[list]:
        with open(self.log_path) as f:
            history = json.load(f)
        return history[-limit:]
