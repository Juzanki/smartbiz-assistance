# === auto_patch_rollback.py — Patch Recovery Logger for SmartInjectGPT ===

import json
import shutil
from pathlib import Path
from datetime import datetime

class PatchRollback:
    def __init__(self, log_file="backend/defense/rollback_log.json"):
        self._log_file = Path(log_file)
        self._log_file.parent.mkdir(parents=True, exist_ok=True)
        if not self._log_file.exists():
            self._log_file.write_text(json.dumps([], indent=2))

    def log(self, message: str, module: str = "unknown", success: bool = True):
        try:
            history = json.loads(self._log_file.read_text())
        except json.JSONDecodeError:
            history = []

        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": module,
            "success": success,
            "message": message
        }
        history.append(entry)
        self._log_file.write_text(json.dumps(history, indent=2))

    def recent_logs(self, limit: int = 5):
        try:
            history = json.loads(self._log_file.read_text())
            return history[-limit:]
        except Exception:
            return []

    def rollback_patch(self, patch_name: str):
        self.log(
            message=f"Rollback triggered for patch: {patch_name}",
            module=patch_name,
            success=True
        )
        return {"status": "rolled back", "patch": patch_name}

    def create_backup(self, code_path: str):
        path = Path(code_path)
        if path.exists():
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{path.stem}_backup_{timestamp}{path.suffix}"
            backup_path = path.parent / backup_name
            shutil.copy(code_path, backup_path)

            self.log(
                message=f"Backup created for {code_path}",
                module=path.name,
                success=True
            )
            return str(backup_path)
        else:
            self.log(
                message=f"Backup failed — file not found: {code_path}",
                module="create_backup",
                success=False
            )
            raise FileNotFoundError(f"{code_path} haipo kwa ajili ya backup.")
