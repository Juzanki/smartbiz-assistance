# watch_all.ps1 — Master Watchdog to launch all defense layers for SmartInjectGPT

Write-Host "`n🧠 Booting Full SmartInjectGPT Defense Suite..." -ForegroundColor Cyan

# Njia za scripts
$rescueScript = "$PSScriptRoot\\auto_rescue.ps1"
$patchScript = "$PSScriptRoot\\auto_patch_checker.ps1"
$selfHealer = "$PSScriptRoot\\SmartSelfHealer.ps1"
$guardian = "$PSScriptRoot\\guardian_layer.ps1"

# Fungua kila script kwenye dirisha tofauti la PowerShell
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy Bypass", "-File", $rescueScript
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy Bypass", "-File", $patchScript
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy Bypass", "-File", $selfHealer
Start-Process powershell -ArgumentList "-NoExit", "-ExecutionPolicy Bypass", "-File", $guardian

Write-Host "`n✅ SmartInjectGPT Defense Suite Now Running on All Layers." -ForegroundColor Green
