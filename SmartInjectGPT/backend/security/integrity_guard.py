# integrity_guard.py — Verifies Module Integrity via Hash Checks

import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List


class IntegrityGuard:
    def __init__(self, watch_paths: List[str], hash_log="SmartInjectGPT/security/integrity_log.json"):
        self.watch_paths = [Path(p) for p in watch_paths]
        self.log_file = Path(hash_log)
        self._init_log()

    def _init_log(self):
        if not self.log_file.exists():
            self.log_file.write_text(json.dumps({}, indent=2))

    def _hash_file(self, file_path: Path) -> str:
        content = file_path.read_bytes()
        return hashlib.sha256(content).hexdigest()

    def store_integrity_snapshot(self) -> Dict:
        integrity = {}
        for path in self.watch_paths:
            if path.exists():
                integrity[str(path)] = self._hash_file(path)

        timestamp = datetime.utcnow().isoformat()
        snapshot = {"timestamp": timestamp, "hashes": integrity}

        self.log_file.write_text(json.dumps(snapshot, indent=2))
        return {"status": "✅ Snapshot Saved", "timestamp": timestamp}

    def verify_integrity(self) -> Dict:
        current = {}
        snapshot = json.loads(self.log_file.read_text())["hashes"]

        for path_str, known_hash in snapshot.items():
            path = Path(path_str)
            if not path.exists():
                current[path_str] = "❌ MISSING"
            else:
                current_hash = self._hash_file(path)
                current[path_str] = "✅ OK" if current_hash == known_hash else "⚠️ ALTERED"

        alerts = {k: v for k, v in current.items() if v != "✅ OK"}
        return {
            "status": "🔍 Checked",
            "summary": f"{len(alerts)} issues detected" if alerts else "All OK",
            "results": current
        }

    def log_event(self, event: str, status: str, details: str = ""):
        print(f"[INTEGRITY-GUARD] {event.upper()} — {status.upper()} — {details}")
