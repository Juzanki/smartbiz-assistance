# scheduler.ps1 — Periodic Runner for SmartInjectGPT Kernel or Watchdog

Write-Host "`n⏰ SmartInjectGPT Scheduler Activated" -ForegroundColor Cyan

$interval = 900 # sekunde 900 = dakika 15
$maxRuns = 99999
$counter = 0

while ($counter -lt $maxRuns) {
    $timeNow = Get-Date -Format "HH:mm:ss"
    Write-Host "`n🕒 [$timeNow] - Cycle $($counter + 1): Launching kernel..." -ForegroundColor Yellow

    # Change to 'launch_kernel.ps1' or 'watch_all.ps1'
    & "$PSScriptRoot\\launch_kernel.ps1"  # au tumia watch_all.ps1

    $counter++
    Start-Sleep -Seconds $interval
}
