# =========================================================
# 🐳 Dockerfile for SmartBiz Assistance (Railway Optimized)
# ✅ No start.sh — direct uvicorn execution
# ✅ Clean structure + safe for production (no .env copying)
# ✅ Relies on Railway Environment Variables
# =========================================================

# 🐍 Lightweight official Python base image
FROM python:3.10-slim

# 📁 Set working directory
WORKDIR /app

# 🔽 Install Python dependencies (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📦 Copy entire app source
COPY . .

# 🌐 UTF-8 Encoding (recommended)
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 🌍 Expose FastAPI default port
EXPOSE 8000

# 🚀 Launch FastAPI with uvicorn (recommended method)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
