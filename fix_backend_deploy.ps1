# =========================
# 🚀 SmartBiz Fix Script: fix_backend_deploy.ps1
# 🔧 Fix Dockerfile CMD + Push to GitHub
# =========================

# 1. Faili ya Dockerfile
$dockerfilePath = ".\Dockerfile"

# 2. Soma content na tafuta line ya CMD
$dockerContent = Get-Content $dockerfilePath

# 3. Badilisha line ya CMD
$fixedContent = $dockerContent -replace 'CMD\s+\[.*\]', 'CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]'

# 4. Andika upya Dockerfile
Set-Content -Path $dockerfilePath -Value $fixedContent
Write-Host "✅ Dockerfile CMD updated to use backend.main:app" -ForegroundColor Green

# 5. Stage changes
git add Dockerfile

# 6. Commit changes
git commit -m "🐳 Fix Dockerfile CMD to backend.main:app for Railway deployment"

# 7. Push changes
git push origin main
Write-Host "🚀 Mabadiliko yamepushwa. Subiri Railway ijideploy automatic..." -ForegroundColor Cyan

# 8. Onyesha link ya backend (kama unajua)
$railwayURL = "https://web-production-5e457.up.railway.app"
Write-Host "`n🌐 Tafadhali tembelea backend yako hapa: $railwayURL" -ForegroundColor Yellow
