# === Prompt Firewall Check (MUST RUN FIRST) ===
$firewallPath = "$PSScriptRoot\prompt_firewall.ps1"

if (Test-Path $firewallPath) {
    & $firewallPath -PromptText $NewCode
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Injection cancelled by firewall." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "⚠️ Firewall script not found. Skipping check..." -ForegroundColor Yellow
}

# === Log Injection (Resolve Safe Paths) ===
$resolvedFilePath   = if ($FilePath)    { (Resolve-Path $FilePath).Path }    else { "N/A" }
$resolvedBackupPath = if ($backupPath)  { (Resolve-Path $backupPath).Path }  else { "N/A" }

$logLine = @{
    file   = $resolvedFilePath
    tag    = $Tag
    backup = $resolvedBackupPath
    time   = $timestamp
} | ConvertTo-Json -Compress

# === Save to Log File ===
$logFilePath = "$PSScriptRoot\..\log\injection_log.json"
if (-not (Test-Path $logFilePath)) {
    New-Item -ItemType File -Path $logFilePath | Out-Null
}
Add-Content -Path $logFilePath -Value $logLine

# === SmartAudit After Injection ===
$relativeAuditPath = "$PSScriptRoot\SmartAudit.ps1"

if (Test-Path $relativeAuditPath -and (Test-Path $backupPath) -and (Test-Path $FilePath)) {
    Write-Host "`n🔍 Running SmartAudit for verification..." -ForegroundColor Cyan
    & $relativeAuditPath `
        -OriginalFile $FilePath `
        -BackupFile $backupPath
}

# === Shadow Tester ===
$shadowTester = "$PSScriptRoot\shadow_tester.ps1"
if (Test-Path $shadowTester) {
    & $shadowTester -CodeText $NewCode
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Injection cancelled by shadow test." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "⚠️ Shadow tester not found. Skipping..." -ForegroundColor Yellow
}
