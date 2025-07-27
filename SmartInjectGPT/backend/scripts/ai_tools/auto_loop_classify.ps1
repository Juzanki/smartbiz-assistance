Write-Host "`n[Loop] Auto Loop Classifier Started..." -ForegroundColor Cyan

$previous = ""

while ($true) {
    try {
        $responsePath = "$PSScriptRoot\..\generated_code.txt"
        $classifierPath = "$PSScriptRoot\auto_classifier.ps1"
        $logPath = "$PSScriptRoot\..\loop_log.txt"

        if (-not (Test-Path $responsePath)) {
            Write-Host "[Warning] generated_code.txt not found!" -ForegroundColor Yellow
            Add-Content -Path $logPath -Value "$(Get-Date) - WARNING: generated_code.txt not found"
        }
        else {
            $current = Get-Content $responsePath -Raw
            if ($current -ne $previous) {
                Write-Host "`n[Info] Detected new content in generated_code.txt..." -ForegroundColor Green
                Add-Content -Path $logPath -Value "$(Get-Date) - New content detected. Running classifier..."

                & $classifierPath

                Add-Content -Path $logPath -Value "$(Get-Date) - Classification script executed successfully."
                $previous = $current
            }
        }
    }
    catch {
        Write-Host "[Error] Failed to execute: $_" -ForegroundColor Red
        Add-Content -Path $logPath -Value "$(Get-Date) - ERROR: $_"
    }

    Start-Sleep -Seconds 5
}
