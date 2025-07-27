param (
    [string]$inputText,
    [string]$tag
)

Write-Host "🚀 Injecting code for tag: $tag"

# Load file_map.json
$jsonPath = Join-Path $PSScriptRoot "file_map.json"
if (-not (Test-Path $jsonPath)) {
    Write-Host "❌ file_map.json not found at: $jsonPath"
    exit 1
}

# Read and extract target relative path
try {
    $json = Get-Content -Path $jsonPath -Raw | ConvertFrom-Json
    $relativePath = $json.$tag
    if (-not $relativePath) {
        Write-Host "❌ Tag [$tag] not found in file_map.json"
        exit 1
    }
} catch {
    Write-Host "❌ Failed to parse file_map.json"
    exit 1
}

# Build full path directly from script location + relative path from JSON
try {
    $targetFullPath = Join-Path $PSScriptRoot $relativePath
    $targetFullPath = [System.IO.Path]::GetFullPath($targetFullPath)
} catch {
    Write-Host "❌ Could not resolve target path."
    exit 1
}

# Prevent self-injection
$injectorPath = (Get-Item $MyInvocation.MyCommand.Path).FullName
if ($injectorPath -eq $targetFullPath) {
    Write-Host "⛔ Cannot inject into injector.ps1 itself."
    exit 1
}

# Ensure parent directory exists
$dir = Split-Path $targetFullPath -Parent
if (-not (Test-Path $dir)) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
}

# Ensure file exists and has tag markers
if (-not (Test-Path $targetFullPath)) {
    Write-Host "ℹ️ Creating new file with tag markers at: $targetFullPath"
    New-Item -ItemType File -Path $targetFullPath -Force | Out-Null
    Add-Content $targetFullPath "`n# ==== GPT_INSERT_START [$tag] ===="
    Add-Content $targetFullPath "`n# ==== GPT_INSERT_END [$tag] ===="
}

# Load content
try {
    $fileText = Get-Content -Path $targetFullPath -Raw
} catch {
    Write-Host "❌ Cannot read file: $targetFullPath"
    exit 1
}

# Define markers
$startTag = "# ==== GPT_INSERT_START [$tag] ===="
$endTag = "# ==== GPT_INSERT_END [$tag] ===="
$pattern = "(?s)(?<=$startTag)(.*?)(?=$endTag)"

# Inject code
if ($fileText -match $pattern) {
    $existing = ($matches[0]).Trim()
    if ($existing -ne "") {
        Write-Host "⚠️ Code already exists for [$tag]. Nothing inserted."
        exit 0
    }

    $updated = [regex]::Replace($fileText, $pattern, "`r`n$inputText`r`n")
    Set-Content -Path $targetFullPath -Value $updated -Encoding UTF8
    Write-Host "✅ Code injected into [$relativePath]"
} else {
    Write-Host "❌ Insert tags not found in file. Expected markers:"
    Write-Host "   $startTag"
    Write-Host "   $endTag"
    exit 1
}
