# test_snapshot_manager.py — Compares Test Results Across Versions

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class TestSnapshotManager:
    def __init__(self, snapshot_dir="SmartInjectGPT/snapshots"):
        self.snapshot_dir = Path(snapshot_dir)
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)

    def _hash_result(self, data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def save_snapshot(self, module_name: str, test_results: dict) -> Dict:
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        filename = f"{module_name}_{timestamp}.json"
        filepath = self.snapshot_dir / filename

        json.dump(test_results, open(filepath, "w"), indent=2)
        hash_val = self._hash_result(json.dumps(test_results, sort_keys=True))

        return {
            "status": "saved",
            "module": module_name,
            "snapshot_file": str(filepath),
            "hash": hash_val
        }

    def compare_snapshots(self, old_path: str, new_path: str) -> Dict:
        old_data = json.load(open(old_path))
        new_data = json.load(open(new_path))

        old_hash = self._hash_result(json.dumps(old_data, sort_keys=True))
        new_hash = self._hash_result(json.dumps(new_data, sort_keys=True))

        changes = {
            "new_tests": [],
            "regressions": [],
            "unchanged": []
        }

        for key in new_data:
            if key not in old_data:
                changes["new_tests"].append(key)
            elif new_data[key] != old_data[key]:
                changes["regressions"].append(key)
            else:
                changes["unchanged"].append(key)

        return {
            "status": "compared",
            "changed": old_hash != new_hash,
            "diff": changes,
            "summary": f"Added: {len(changes['new_tests'])}, Regressed: {len(changes['regressions'])}, Stable: {len(changes['unchanged'])}"
        }
