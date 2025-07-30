# =========================================================
# 🐳 Dockerfile for SmartBiz Assistance (Railway Optimized)
# ✅ No start.sh — direct uvicorn execution
# ✅ Clean structure + safe for production
# =========================================================

# 🐍 Base Python image
FROM python:3.10-slim

# 📁 Set working directory
WORKDIR /app

# 📋 Copy and install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 🗂️ Copy the entire app code
COPY . .

# 🌐 Environment settings to handle encoding
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 🌍 Expose FastAPI default port (used by Railway)
EXPOSE 8000

# 🚀 Start FastAPI using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
