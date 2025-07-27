# launch_kernel.ps1

Write-Host "`n🚀 Launching SmartInjectGPT Kernel..." -ForegroundColor Cyan

$promptPath = "$PSScriptRoot\..\input_dream.txt"
$logPath = "$PSScriptRoot\..\result_log.txt"
$scriptPath = "$PSScriptRoot\run_kernel.py"

if (!(Test-Path $promptPath)) {
    Write-Host "⚠️ Prompt file haijapatikana: $promptPath" -ForegroundColor Yellow
    exit
}

Write-Host "🧠 Reading prompt from: $promptPath" -ForegroundColor Green
Write-Host "📦 Executing: $scriptPath" -ForegroundColor Blue

try {
    $results = & python "$scriptPath" 2>&1
    $results | Tee-Object -FilePath $logPath
    Write-Host "`n✅ Kernel executed. Logs saved to: $logPath" -ForegroundColor Green
}
catch {
    Write-Host "`n❌ Hitilafu imetokea kwenye kernel!" -ForegroundColor Red
    $_ | Out-File -FilePath $logPath -Encoding utf8
}
