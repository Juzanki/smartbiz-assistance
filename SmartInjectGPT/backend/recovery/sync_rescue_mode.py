# SyncRescueMode — AI Silent Survival + Auto Sync for SmartInjectGPT

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import List

class SyncRescueMode:
    def __init__(self, backup_path="SmartInjectGPT/secure/emergency_backup.json"):
        self.backup_path = Path(backup_path)
        self.cache: List[dict] = []
        self.offline = False

    def enter_silent_mode(self):
        self.offline = True
        logging.warning("[RESCUE] Silent mode activated. AI will not respond or inject.")
    
    def exit_silent_mode(self):
        self.offline = False
        logging.info("[RESCUE] Silent mode exited. Auto-sync initiating.")
        self.auto_sync()

    def cache_action(self, label: str, payload: str):
        if not self.offline:
            return False
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "label": label,
            "payload": payload
        }
        self.cache.append(entry)
        self._save_backup()
        logging.info(f"[RESCUE] Action cached: {label}")
        return True

    def _save_backup(self):
        self.backup_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.backup_path, "w") as f:
            json.dump(self.cache, f, indent=2)

    def auto_sync(self):
        if not self.cache:
            logging.info("[RESCUE] No cached actions to sync.")
            return
        for entry in self.cache:
            print(f"[AUTO-SYNC] Restoring: {entry['label']} @ {entry['timestamp']}")
        self.cache.clear()
        self._save_backup()
        logging.info("[RESCUE] Auto-sync complete.")
