# ===============================
# 📦 SmartBiz Push Automation
# ===============================
$frontend = "E:\SmartBiz_Assistance\smartbiz-landing"
$backend = "E:\SmartBiz_Assistance\backend"

Function Push-IfChanged($path, $projectName) {
    Write-Host "📁 Checking: $projectName ($path)" -ForegroundColor Cyan
    Set-Location $path
    $status = git status --porcelain
    if ($status) {
        Write-Host "`n🔍 Changes detected in $projectName:`n" -ForegroundColor Yellow
        $status | Out-String | Write-Host

        $confirm = Read-Host "✅ Do you want to commit and push $projectName changes? (y/n)"
        if ($confirm -eq 'y') {
            $commitMessage = Read-Host "📝 Enter commit message for $projectName"
            git add .
            git commit -m "$commitMessage"
            git push origin main
            Write-Host "🚀 $projectName pushed successfully!" -ForegroundColor Green
        } else {
            Write-Host "⏭️ Skipping $projectName..." -ForegroundColor DarkGray
        }
    } else {
        Write-Host "✅ No changes detected in $projectName." -ForegroundColor Green
    }
}

Push-IfChanged -path $frontend -projectName "Frontend"
Push-IfChanged -path $backend -projectName "Backend"
