# guardian_layer.ps1 — Tamper & Integrity Watchdog for SmartInjectGPT

Write-Host "`n🛡️ Guardian Layer Activated... Monitoring SmartInjectGPT Files..." -ForegroundColor Cyan

# Orodha ya mafaili muhimu ya kulindwa
$watchedFiles = @(
    "..\\kernel\\smartinject_kernel.py",
    "..\\input_dream.txt",
    "..\\scripts\\ai_tools\\injection_engine.ps1",
    "..\\identity\\soul_signature.py"
)

# Kipindi cha kuangalia kila sekunde ngapi
$interval = 5

# Hifadhi timestamps za awali
$fileStamps = @{}

foreach ($file in $watchedFiles) {
    if (Test-Path $file) {
        $fileStamps[$file] = (Get-Item $file).LastWriteTime
    }
}

Write-Host "📡 Initial snapshot taken. Now watching for changes..." -ForegroundColor Blue

while ($true) {
    foreach ($file in $watchedFiles) {
        if (Test-Path $file) {
            $currentTime = (Get-Item $file).LastWriteTime
            if ($fileStamps[$file] -ne $currentTime) {
                Write-Host "⚠️ ALERT: File tampering detected: $file" -ForegroundColor Red
                # Rudi kwa backup au changanua kwa integrity
                python "..\\defense\\auto_patch_rollback.py"
                python "..\\security\\integrity_guard.py"
                $fileStamps[$file] = $currentTime
            }
        } else {
            Write-Host "❌ FILE MISSING: $file" -ForegroundColor Yellow
        }
    }

    Start-Sleep -Seconds $interval
}
