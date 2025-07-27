param (
    [string]$responseText
)

Write-Host "`n🔍 Parsing response and injecting code..." -ForegroundColor Cyan

# Soma file_map.json
$jsonPath = Join-Path $PSScriptRoot "file_map.json"
if (-not (Test-Path $jsonPath)) {
    Write-Host "❌ file_map.json not found!" -ForegroundColor Red
    exit 1
}

try {
    $json = Get-Content -Raw -Path $jsonPath | ConvertFrom-Json
} catch {
    Write-Host "❌ file_map.json is invalid!" -ForegroundColor Red
    exit 1
}

# Regex ya kupata tag na code
$pattern = "# === BEGIN \[(.+?)\] ===\r?\n(.*?)\r?\n# === END \[\1\] ==="
$matches = [regex]::Matches($responseText, $pattern, 'Singleline')

foreach ($match in $matches) {
    $tag = $match.Groups[1].Value
    $code = $match.Groups[2].Value.Trim()

    if (-not ($json.PSObject.Properties.Name -contains $tag)) {
        Write-Host "⚠️  Tag [$tag] not found in file_map.json." -ForegroundColor Yellow
        continue
    }

    $relPath = $json[$tag]
    $absPath = Join-Path $PSScriptRoot "..\..\$relPath"
    if (-not (Test-Path $absPath)) {
        Write-Host "ℹ️ File not found. Creating: $absPath"
        New-Item -ItemType File -Path $absPath -Force | Out-Null
        Add-Content -Path $absPath -Value "`n# ==== GPT_INSERT_START [$tag] ===="
        Add-Content -Path $absPath -Value "`n# ==== GPT_INSERT_END [$tag] ===="
    }

    $fileText = Get-Content -Raw -Path $absPath
    $startMarker = "# ==== GPT_INSERT_START [$tag] ===="
    $endMarker = "# ==== GPT_INSERT_END [$tag] ===="

    if ($fileText -match [regex]::Escape($startMarker) -and $fileText -match [regex]::Escape($endMarker)) {
        $newContent = $fileText -replace "(?s)(?<=" + [regex]::Escape($startMarker) + ")(.*?)(?=" + [regex]::Escape($endMarker) + ")", "`r`n$code`r`n"
        Set-Content -Path $absPath -Value $newContent -Encoding UTF8
        Write-Host "✅ Code injected for [$tag] into $relPath" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Markers not found for [$tag], reinserting markers..." -ForegroundColor Yellow
        Add-Content -Path $absPath -Value "`n$startMarker`r`n$code`r`n$endMarker"
    }
}

Write-Host "`n✅ Done!"
