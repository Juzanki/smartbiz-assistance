Write-Host "`n🔍 SMARTINJECTGPT KERNEL STATUS CHECK" -ForegroundColor Cyan

$logPath = "SmartInjectGPT/logs/server.log"

if (-Not (Test-Path $logPath)) {
    Write-Host "❌ Log file not found at: $logPath" -ForegroundColor Red
    exit 1
}

$logContent = Get-Content $logPath -Tail 50

$checks = @{
    "Permissions loaded"               = "✅ Permissions OK"
    "INIT_KERNEL - INITIALIZED"        = "✅ Kernel Boot OK"
    "Memory"                           = "✅ Memory OK"
    "Firewall"                         = "✅ Firewall OK"
    "WATCHDOG"                         = "✅ Watchdog OK"
    "Dream interpreted"                = "✅ Dream Interpreter OK"
    "TEST_RESULTS - EVALUATED"         = "✅ Module Test Passed"
    "DEPLOYMENT - SUCCESS"             = "✅ Deployment OK"
    "DIVINE"                           = "✅ Divine Signature Verified"
    "Kernel initialized successfully"  = "✅ Final Kernel OK"
}

$errors = @()
foreach ($key in $checks.Keys) {
    if ($logContent -match [regex]::Escape($key)) {
        Write-Host $checks[$key] -ForegroundColor Green
    } else {
        Write-Host "❓ Missing: $key" -ForegroundColor Yellow
        $errors += $key
    }
}

if ($errors.Count -eq 0) {
    Write-Host "`n✅ All kernel systems are operational." -ForegroundColor Cyan
} else {
    Write-Host "`n❌ Issues detected with:" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" -ForegroundColor Red }
}

Write-Host "`n💡 Tip: Use --reload-dir to avoid infinite loops." -ForegroundColor DarkGray
