# === Define paths ===
$defenseDir = "E:\SmartBiz_Assistance\SmartInjectGPT\backend\defense"
$targetFile = Join-Path $defenseDir "auto_patch_rollback.py"
$backupFile = Join-Path $defenseDir "auto_patch_rollback_backup_$(Get-Date -Format 'yyyyMMdd-HHmmss').py"

# === Ensure directory exists ===
if (-Not (Test-Path $defenseDir)) {
    Write-Host "Creating defense folder..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $defenseDir -Force | Out-Null
}

# === Backup old version if exists ===
if (Test-Path $targetFile) {
    Copy-Item $targetFile -Destination $backupFile
    Write-Host "✅ Backup created: $backupFile" -ForegroundColor Cyan
}

# === Define new fixed code ===
$fixedCode = @"
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
"@

# === Write fixed code ===
$fixedCode | Out-File -FilePath $targetFile -Encoding UTF8 -Force
Write-Host "✅ Fixed version written to: $targetFile" -ForegroundColor Green
