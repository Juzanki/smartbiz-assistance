# auto_rescue.ps1 - SmartInjectGPT Auto Recovery Script

Write-Host "`n🛡️ Auto Rescue Mode Activated..." -ForegroundColor Cyan

$logPath = "$PSScriptRoot\..\result_log.txt"
$threshold = 3 # max allowed failures
$failCount = 0

# Soma log kama ipo
if (Test-Path $logPath) {
    $log = Get-Content $logPath -Raw

    if ($log -match "❌|ROLLBACK|EMERGENCY") {
        $failCount += 1
        Write-Host "⚠️ Failure detected in log!" -ForegroundColor Yellow
    }
}

# Chukua hatua endapo failure ni nyingi
if ($failCount -ge $threshold) {
    Write-Host "🚨 Triggering Auto Recovery..." -ForegroundColor Red
    # Fanya recovery ya kernel na identity
    python "../backend/defense/ai_self_shield.py"
    python "../backend/core/resurrector.py"
}
else {
    Write-Host "✅ System is stable." -ForegroundColor Green
}
