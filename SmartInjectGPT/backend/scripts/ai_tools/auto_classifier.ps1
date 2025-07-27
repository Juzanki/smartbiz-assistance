Write-Host "`n🚀 Running auto_classifier.ps1..." -ForegroundColor Cyan

$responsePath = "$PSScriptRoot\..\generated_code.txt" -replace '\\ai_tools$', ''
$fileMapPath  = "$PSScriptRoot\..\file_map.json"

if (-not (Test-Path $responsePath)) {
    Write-Host "❌ generated_code.txt not found!" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $fileMapPath)) {
    Write-Host "❌ file_map.json not found!" -ForegroundColor Red
    exit 1
}

$response = Get-Content $responsePath -Raw
$tag = "frontend:gifts_ui"

# Optional: Match content and adjust tag
if ($response -match "GiftViewer|gift") {
    $tag = "frontend:gifts_ui"
}
elseif ($response -match "LoginPage") {
    $tag = "frontend:login_ui"
}
elseif ($response -match "DashboardOwner") {
    $tag = "frontend:dashboard_owner"
}
# Add more matching rules here as needed

try {
    $payload = @{
        tag      = $tag
        response = $response
    } | ConvertTo-Json -Depth 3

    $res = Invoke-RestMethod -Uri "http://127.0.0.1:8000/smartinject/inject" `
        -Method Post `
        -Body $payload `
        -ContentType "application/json"

    Write-Host "✅ Injected successfully: $($res.message)" -ForegroundColor Green
}
catch {
    Write-Host "❌ Failed to inject: $_" -ForegroundColor Red
}
