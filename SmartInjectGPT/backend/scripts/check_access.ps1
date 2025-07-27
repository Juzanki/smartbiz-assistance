# === check_access.ps1 ===
param (
    [string]$Username,
    [string]$UserIP = "127.0.0.1",
    [string]$MfaCode,
    [string]$AccessKey
)

$permPath = "$PSScriptRoot\..\auth\permissions.json"
if (-not (Test-Path $permPath)) {
    Write-Host "❌ Permissions file not found." -ForegroundColor Red
    exit 1
}

# Load permissions
$json = Get-Content -Raw -Path $permPath | ConvertFrom-Json
if (-not $json.$Username) {
    Write-Host "❌ User not found in permissions." -ForegroundColor Red
    exit 1
}

$user = $json.$Username

# IP Check
if ($user.ip_whitelist.Count -gt 0 -and $UserIP -notin $user.ip_whitelist) {
    Write-Host "❌ IP address $UserIP not allowed for $Username" -ForegroundColor Red
    exit 1
}

# MFA Check (basic pattern check)
if ($user.mfa_enabled -eq $true -and ($MfaCode -ne "777999")) {
    Write-Host "❌ Invalid MFA code for $Username" -ForegroundColor Red
    exit 1
}

# Temporal Window Check (e.g., only 10:00–10:10 UTC allowed)
$now = (Get-Date).ToUniversalTime()
$allowedStart = Get-Date "$($now.ToString('yyyy-MM-dd'))T10:00:00Z"
$allowedEnd = Get-Date "$($now.ToString('yyyy-MM-dd'))T10:10:00Z"

if ($now -lt $allowedStart -or $now -gt $allowedEnd) {
    Write-Host "❌ Access denied: Outside of temporal access window (10:00–10:10 UTC)" -ForegroundColor Red
    exit 1
}

# AccessKey (Optional: SpiritualKeyAuth hashed)
if ($AccessKey -ne "PROPHETIC2025") {
    Write-Host "❌ Invalid spiritual access key." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Access granted to $Username at $($now.ToShortTimeString()) UTC" -ForegroundColor Green
