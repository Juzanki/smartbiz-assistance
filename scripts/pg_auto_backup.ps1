# === pg_auto_backup.ps1 ===

# Set variables
$pgBinPath = "C:\Program Files\PostgreSQL\15\bin"  # badilisha version yako hapa
$backupFolder = "E:\SmartBiz_Backups"
$date = Get-Date -Format "yyyy-MM-dd"
$fileName = "pg_backup_$date.sql"
$outputPath = Join-Path $backupFolder $fileName

# Ensure backup folder exists
if (!(Test-Path $backupFolder)) {
    New-Item -Path $backupFolder -ItemType Directory
}

# Add PostgreSQL bin to path for pg_dump
$env:Path += ";$pgBinPath"

# Run pg_dump
pg_dump -U postgres -d smartbiz_db -h localhost -p 5432 -F p -f $outputPath

# Feedback
if (Test-Path $outputPath) {
    Write-Host "✅ PostgreSQL backup created at $outputPath"
} else {
    Write-Host "❌ Backup failed!"
}
