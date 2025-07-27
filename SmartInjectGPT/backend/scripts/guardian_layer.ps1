# === guardian_layer.ps1 ===
param (
    [string]$TargetFile,
    [string]$Tag = "unspecified"
)

Write-Host "`n⚠️  GUARDIAN ALERT ⚠️" -ForegroundColor Yellow
Write-Host "Unataka kubadilisha file: $TargetFile"
Write-Host "Kwa tag: $Tag"
Write-Host "Je una uhakika kweli? (Y/N): " -NoNewline

$userInput = Read-Host

if ($userInput -ne "Y" -and $userInput -ne "y") {
    Write-Host "`n❌ Injection imekatishwa na Guardian Layer." -ForegroundColor Red
    exit 1
}

Write-Host "`n✅ Ruhusa imetolewa. Injection itaendelea..." -ForegroundColor Green
