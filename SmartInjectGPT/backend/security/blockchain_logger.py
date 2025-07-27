# backend/security/blockchain_logger.py

import json
from pathlib import Path
from datetime import datetime

class BlockchainLogger:
    def __init__(self, path: str = "backend/security/chain_log.json"):
        self.log_path = Path(path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_path.exists():
            self._init_chain()

    def _init_chain(self):
        genesis = {
            "chain": [
                {
                    "index": 0,
                    "timestamp": str(datetime.utcnow()),
                    "action": "Genesis Block",
                    "data": {}
                }
            ]
        }
        self._write_chain(genesis)

    def _write_chain(self, data):
        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _read_chain(self):
        with open(self.log_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def append_block(self, action: str, data: dict):
        chain = self._read_chain()["chain"]
        new_block = {
            "index": len(chain),
            "timestamp": str(datetime.utcnow()),
            "action": action,
            "data": data
        }
        chain.append(new_block)
        self._write_chain({"chain": chain})
        print(f"🧾 Block added: {action}")
