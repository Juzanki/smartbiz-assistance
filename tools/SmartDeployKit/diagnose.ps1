param ()

Write-Host "`n🔍 Running SmartDeployKit Diagnostic..." -ForegroundColor Cyan

# 1. Load file_map.json
$jsonPath = Join-Path $PSScriptRoot "file_map.json"
if (-not (Test-Path $jsonPath)) {
    Write-Host "❌ file_map.json not found!" -ForegroundColor Red
    exit 1
}

try {
    $json = Get-Content -Path $jsonPath -Raw | ConvertFrom-Json
    Write-Host "✅ file_map.json loaded successfully." -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to parse file_map.json" -ForegroundColor Red
    exit 1
}

# 2. Check every tag → file path
foreach ($key in $json.PSObject.Properties.Name) {
    $relPath = $json.$key
    $base = Resolve-Path "$PSScriptRoot\..\.."
    $absPath = Join-Path $base $relPath

    if (-not (Test-Path $absPath)) {
        Write-Host "❌ [$key] file not found → $absPath" -ForegroundColor Red
        continue
    } else {
        Write-Host "✅ [$key] file found → $absPath" -ForegroundColor Green
    }

    # 3. Check insert tags
    try {
        $fileText = Get-Content $absPath -Raw
        $start = "# ==== GPT_INSERT_START [$key] ===="
        $end = "# ==== GPT_INSERT_END [$key] ===="

        if ($fileText -match [regex]::Escape($start) -and $fileText -match [regex]::Escape($end)) {
            Write-Host "✅ [$key] has valid insert tags." -ForegroundColor Green
        } else {
            Write-Host "⚠️ [$key] missing insert tags." -ForegroundColor Yellow
        }
    } catch {
        Write-Host "❌ [$key] failed to read content." -ForegroundColor Red
    }
}

Write-Host "✅ Diagnostic finished." -ForegroundColor Cyan

