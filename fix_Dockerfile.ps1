# ============================================
# ✅ Fix Dockerfile for SmartBiz Assistance
#    Deletes old and creates fresh with correct config
# ============================================

$dockerfilePath = "Dockerfile"

# 1. ⚠️ Delete existing Dockerfile if it exists
if (Test-Path $dockerfilePath) {
    Remove-Item $dockerfilePath -Force
    Write-Host "🗑️ Deleted old Dockerfile"
}

# 2. ✍️ Create new Dockerfile with correct config
@'
# ====================================================
# ? Dockerfile for SmartBiz Assistance (Railway Ready)
# ====================================================

# ?? Lightweight official Python base image
FROM python:3.10-slim

# ?? Set working directory
WORKDIR /app

# ?? Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ?? Copy entire app
COPY . .

# ?? Set UTF-8 encoding
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# ?? Expose FastAPI port
EXPOSE 8000

# ?? Launch FastAPI using uvicorn from backend.main
CMD ["sh", "-c", "uvicorn backend.main:app --host=0.0.0.0 --port=${PORT:-8000}"]
'@ | Out-File -Encoding utf8 -FilePath $dockerfilePath

Write-Host "✅ Dockerfile created successfully with updated configuration"
