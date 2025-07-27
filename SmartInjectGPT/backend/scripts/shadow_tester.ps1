# === shadow_tester.ps1 ===
param (
    [string]$CodeText,
    [string]$Lang = "python"
)

$tempFile = "$env:TEMP\smartinject_shadow_test.py"
Set-Content -Path $tempFile -Value $CodeText -Encoding UTF8

Write-Host "`n👻 Shadow testing code..." -ForegroundColor DarkCyan

try {
    if ($Lang -eq "python") {
        python -m py_compile $tempFile 2>&1 | ForEach-Object {
            if ($_ -ne "") {
                Write-Host "`n❌ Shadow Test Failed!" -ForegroundColor Red
                Write-Host "Error: $_" -ForegroundColor Red
                Remove-Item $tempFile -Force
                exit 1
            }
        }
    }
}
catch {
    Write-Host "`n❌ Exception during shadow test: $_" -ForegroundColor Red
    Remove-Item $tempFile -Force
    exit 1
}

Remove-Item $tempFile -Force
Write-Host "`n✅ Shadow Test Passed – Code is syntactically clean." -ForegroundColor Green
