# auto_patch_rollback.py — Smart Auto Rollback of Faulty Patches

import shutil
from pathlib import Path
from datetime import datetime
import json


class PatchRollback:
    def __init__(self, backup_dir="SmartInjectGPT/backups", log_file="SmartInjectGPT/defense/rollback_log.json"):
        self.backup_path = Path(backup_dir)
        self.backup_path.mkdir(parents=True, exist_ok=True)
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.write_text(json.dumps([]))

    def create_backup(self, module_path: str) -> dict:
        src = Path(module_path)
        if not src.exists():
            return {"status": "❌", "message": "Module file not found."}

        backup_file = self.backup_path / f"{src.stem}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.bak.py"
        shutil.copy(src, backup_file)

        return {
            "status": "✅ Backup created",
            "backup": str(backup_file)
        }

    def rollback(self, module_path: str, backup_file: str) -> dict:
        try:
            dst = Path(module_path)
            src = Path(backup_file)
            if not src.exists():
                return {"status": "❌", "message": "Backup not found."}
            shutil.copy(src, dst)

            entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "module": dst.name,
                "restored_from": str(src),
                "status": "rolled_back"
            }
            self._log(entry)

            return {"status": "✅ Rolled Back", "restored_module": dst.name}
        except Exception as e:
            return {"status": "❌", "error": str(e)}

    def _log(self, entry: dict):
        history = json.loads(self.log_file.read_text())
        history.append(entry)
        self.log_file.write_text(json.dumps(history, indent=2))

    def recent_rollbacks(self, limit: int = 5):
        return json.loads(self.log_file.read_text())[-limit:]
