# cloud_backup.py — Backup SmartInjectGPT core files to /backups folder

import shutil
import os
from datetime import datetime
from pathlib import Path

# Files/folders to backup
BACKUP_ITEMS = [
    "backend/kernel/smartinject_kernel.py",
    "backend/identity/soul_signature.json",
    "backend/prophecy/dream_logs.txt",
    "backend/security/chain_log.json",
    "backend/ethics/smartinject_pledge.txt"
]

# Destination base
DESTINATION_BASE = "SmartInjectGPT/cloud_backups"

def create_backup():
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path(DESTINATION_BASE) / f"backup_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)

    copied = []

    for item in BACKUP_ITEMS:
        src = Path(item)
        if src.exists():
            dst = backup_dir / src.name
            shutil.copy(src, dst)
            copied.append(str(dst))
        else:
            print(f"⚠️ Skipped (not found): {src}")

    return {
        "status": "✅ Backup Complete",
        "location": str(backup_dir),
        "files": copied,
        "timestamp": timestamp
    }

if __name__ == "__main__":
    result = create_backup()
    print(result)
