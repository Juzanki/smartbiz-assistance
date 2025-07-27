# === check_permission.ps1 ===
param (
    [string]$Username,
    [string]$TargetModule,
    [string]$UserIP = "127.0.0.1"
)

$permPath = "$PSScriptRoot\..\auth\permissions.json"

if (-not (Test-Path $permPath)) {
    Write-Host "❌ Permissions file not found." -ForegroundColor Red
    exit 1
}

$json = Get-Content -Path $permPath -Raw | ConvertFrom-Json

if (-not $json.$Username) {
    Write-Host "❌ User '$Username' not found in permissions." -ForegroundColor Red
    exit 1
}

$user = $json.$Username
$role = $user.role
$allowedModules = $user.allowed_modules
$ipWhitelist = $user.ip_whitelist

# IP whitelist check
if ($ipWhitelist.Count -gt 0 -and $UserIP -notin $ipWhitelist) {
    Write-Host "❌ IP $UserIP not allowed for user $Username." -ForegroundColor Red
    exit 1
}

# Module access check
if ($allowedModules -notcontains "*" -and $allowedModules -notcontains $TargetModule) {
    Write-Host "❌ User '$Username' is not allowed to inject into module '$TargetModule'." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Permission check passed for $Username ($role)." -ForegroundColor Green
