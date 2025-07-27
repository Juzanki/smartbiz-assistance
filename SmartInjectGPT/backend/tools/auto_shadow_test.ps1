# auto_shadow_test.ps1 — SmartInjectGPT Shadow Injection Validator

Write-Host "`n🧪 Starting Shadow Injection Test..." -ForegroundColor Cyan

$testTarget = "$PSScriptRoot\..\..\generated_code.txt"
if (!(Test-Path $testTarget)) {
    Write-Host "⚠️ Hakuna module mpya ya kujaribu: $testTarget" -ForegroundColor Yellow
    exit
}

# Soma jina la module
$lines = Get-Content $testTarget
$firstLine = $lines | Select-Object -First 1
if ($firstLine -match "# module: (.+)") {
    $module = $matches[1]
    Write-Host "🧠 Module Detected: $module" -ForegroundColor Green
}
else {
    Write-Host "❌ Hakuna module iliyobainika kwenye generated_code.txt" -ForegroundColor Red
    exit
}

# Tekeleza injection validator
$python = "python"
$shadowTest = "..\defense\shadow_tester.py"
Write-Host "🔍 Running $shadowTest for $module..." -ForegroundColor Blue

try {
    $result = & $python $shadowTest $module 2>&1
    $result | Tee-Object -FilePath "$PSScriptRoot\shadow_test_log.txt"
    Write-Host "`n✅ Shadow Test Completed. Log saved." -ForegroundColor Green
}
catch {
    Write-Host "`n❌ Hitilafu kwenye Shadow Test!" -ForegroundColor Red
}
