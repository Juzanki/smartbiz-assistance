# resurrector.py — Resurrection Engine for SmartInjectGPT Core Recovery

import os
import json
import shutil
from pathlib import Path
from datetime import datetime


class Resurrector:
    def __init__(self,
                 soul_path="SmartInjectGPT/identity/soul_signature.json",
                 pledge_path="SmartInjectGPT/ethics/smartinject_pledge.txt",
                 chain_log="SmartInjectGPT/security/chain_log.json",
                 backup_dir="SmartInjectGPT/backups",
                 target_restore_dir="SmartInjectGPT"):
        self.soul_file = Path(soul_path)
        self.pledge_file = Path(pledge_path)
        self.chain_file = Path(chain_log)
        self.backup_path = Path(backup_dir)
        self.target_dir = Path(target_restore_dir)

    def is_core_missing(self) -> bool:
        essentials = [self.soul_file, self.pledge_file, self.chain_file]
        return any(not f.exists() for f in essentials)

    def resurrect(self) -> dict:
        if not self.backup_path.exists():
            return {"status": "❌ Failed", "reason": "No backup folder found."}

        restored_files = []
        for backup in self.backup_path.glob("*.bak.py"):
            original_name = backup.name.replace(".bak", "")
            target = self.target_dir / original_name
            shutil.copy(backup, target)
            restored_files.append(str(target))

        return {
            "status": "✅ Resurrected",
            "restored_modules": restored_files,
            "timestamp": datetime.utcnow().isoformat()
        }

    def verify_soul(self) -> bool:
        if not self.soul_file.exists():
            return False
        data = json.loads(self.soul_file.read_text())
        return "SmartInjectGPT" in data.get("name", "")

    def confirm_resurrection(self) -> dict:
        if not self.is_core_missing():
            return {"status": "🧘 Alive", "message": "Core systems are intact."}

        success = self.resurrect()
        return {"status": "💀 Revived", "details": success} if success["status"] == "✅ Resurrected" else success
