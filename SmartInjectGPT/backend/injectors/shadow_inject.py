# shadow_inject.py — Stealth Mode Injection System for Testing Modules in Sandbox

import shutil
from pathlib import Path
from datetime import datetime
import json

class ShadowInjector:
    def __init__(self, sandbox_dir="backend/sandbox", log_file="backend/injectors/shadow_log.json"):
        self.sandbox = Path(sandbox_dir)
        self.log_file = Path(log_file)

        # Ensure folders exist
        self.sandbox.mkdir(parents=True, exist_ok=True)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        # Create empty log file if it doesn't exist
        if not self.log_file.exists():
            self.log_file.write_text(json.dumps([], indent=2))

    def inject_to_sandbox(self, module_path: str) -> dict:
        src = Path(module_path)
        if not src.exists():
            return {"status": "❌ Failed", "reason": "File not found"}

        dst = self.sandbox / src.name
        shutil.copy(src, dst)

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "module": src.name,
            "status": "injected",
            "path": str(dst)
        }
        self._log(log_entry)

        return {
            "status": "✅ Injected to Sandbox",
            "file": str(dst),
            "note": "Module injected silently for internal testing."
        }

    def cleanup_sandbox(self) -> dict:
        files = list(self.sandbox.glob("*"))
        for f in files:
            f.unlink()
        return {"status": "cleared", "deleted_files": len(files)}

    def _log(self, entry: dict):
        try:
            history = json.loads(self.log_file.read_text())
        except json.JSONDecodeError:
            history = []

        history.append(entry)
        self.log_file.write_text(json.dumps(history, indent=2))

    def recent_shadow_logs(self, limit: int = 5):
        try:
            history = json.loads(self.log_file.read_text())
            return history[-limit:]
        except Exception:
            return []
