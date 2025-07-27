# === daily_backup.ps1 ===
$sourcePath = "E:\SmartBiz_Assistance"
$backupFolder = "E:\SmartBiz_Backups"
$date = Get-Date -Format "yyyy-MM-dd"
$zipName = "SmartBiz_Backup_$date.zip"
$zipPath = Join-Path $backupFolder $zipName

# Hakikisha backup folder ipo
if (!(Test-Path $backupFolder)) {
    New-Item -Path $backupFolder -ItemType Directory
}

# Funga zip backup
Compress-Archive -Path "$sourcePath\*" -DestinationPath $zipPath -Force

Write-Host "✅ Backup imekamilika: $zipPath"
