# === SmartAudit.ps1 ===
param (
    [string]$OriginalFile,   # e.g. ..\backend\crud\user_crud.py
    [string]$BackupFile      # e.g. ..\backups\2025-05-14\user_crud.py.backup_20250514T123456
)

if (-not (Test-Path $OriginalFile)) {
    Write-Host "❌ Original file not found: $OriginalFile" -ForegroundColor Red
    exit
}
if (-not (Test-Path $BackupFile)) {
    Write-Host "❌ Backup file not found: $BackupFile" -ForegroundColor Red
    exit
}

Write-Host "`n🔍 Running SmartAudit..." -ForegroundColor Cyan
Write-Host "Comparing:" -ForegroundColor Gray
Write-Host "  🔸 $OriginalFile"
Write-Host "  🔸 $BackupFile`n"

$originalLines = Get-Content $OriginalFile
$backupLines = Get-Content $BackupFile

$diff = Compare-Object -ReferenceObject $backupLines -DifferenceObject $originalLines -IncludeEqual -PassThru

$added = 0
$removed = 0

foreach ($line in $diff) {
    if ($line.SideIndicator -eq "=>") {
        Write-Host "+ $line" -ForegroundColor Green
        $added++
    } elseif ($line.SideIndicator -eq "<=") {
        Write-Host "- $line" -ForegroundColor Red
        $removed++
    }
}

Write-Host "`n📊 Summary:"
Write-Host "🟢 Mistari imeongezwa: $added"
Write-Host "🔴 Mistari imeondolewa: $removed"
