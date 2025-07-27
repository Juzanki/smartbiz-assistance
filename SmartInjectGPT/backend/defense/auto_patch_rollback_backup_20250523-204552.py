# auto_patch_rollback.py — Patch Recovery Logger for SmartInjectGPT

import json
from pathlib import Path
from datetime import datetime

class PatchRollback:
    def __init__(self, log_file="backend/defense/rollback_log.json"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_file.exists():
            self.log_file.write_text(json.dumps([], indent=2))

    def log(self, message, module="", success=True):
        try:
            history = json.loads(self.log_file.read_text())
        except json.JSONDecodeError:
            history = []

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": module,
            "success": success,
            "message": message
        }

        history.append(entry)
        self.log_file.write_text(json.dumps(history, indent=2))

    def recent_logs(self, limit=5):
        try:
            history = json.loads(self.log_file.read_text())
            return history[-limit:]
        except Exception:
            return []

    def rollback_patch(self, patch_name):
        self.log(
            message=f"Rollback triggered for patch: {patch_name}",
            module=patch_name,
            success=True
        )
        return {"status": "rolled back", "patch": patch_name}
