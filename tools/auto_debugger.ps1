# 🔧 SmartBiz Auto-Fix Debugger v2.0
Write-Host "`n🚨 SmartBiz Auto-Debugger Starting..." -ForegroundColor Cyan

# === Step 1: Define Paths ===
$initFilePath = "E:\SmartBiz_Assistance\backend\crud\__init__.py"
$mainPath = "E:\SmartBiz_Assistance\backend\main.py"
$logFilePath = "E:\SmartBiz_Assistance\backend\debug_fix_log.txt"
$backupFilePath = "$initFilePath.bak"

# === Step 2: Backup __init__.py ===
if (Test-Path $initFilePath) {
    Copy-Item $initFilePath $backupFilePath -Force
    Write-Host "🛡️ Backup created: $backupFilePath"
}

# === Step 3: Clean __init__.py from circular imports ===
$content = Get-Content $initFilePath
$newContent = $content | Where-Object { $_ -notmatch "from .*user_crud" }
$newContent = @("# __init__.py cleaned by SmartBiz Auto-Debugger") + $newContent
$newContent | Set-Content $initFilePath
Write-Host "✅ Circular imports removed from __init__.py"

# === Step 4: Sanitize main.py imports ===
if (Test-Path $mainPath) {
    $mainContent = Get-Content $mainPath
    $patched = $mainContent -replace "from backend\.crud import", "from backend.crud.user_crud import"
    $patched | Set-Content $mainPath
    Write-Host "🔄 main.py imports sanitized to avoid circular import"
}

# === Step 5: Log Fix ===
if ($logFilePath) {
    Add-Content -Path $logFilePath -Value "$(Get-Date) - Fixed circular imports in __init__.py and sanitized main.py"
    Write-Host "📄 Fix logged in: $logFilePath"
}

# === Step 6: Restart Backend Server ===
Write-Host "`n🚀 Restarting backend server..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd E:\SmartBiz_Assistance; uvicorn backend.main:app --reload"
