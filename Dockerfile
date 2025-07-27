# =========================================================
# 🐳 Dockerfile for SmartBiz Assistance (Production Ready)
# ✅ Railway-compatible + Auto Migration + Clean Structure
# =========================================================

# 🐍 Base Python image (lightweight)
FROM python:3.10-slim

# 📂 Working directory inside the container
WORKDIR /app

# 📋 Copy only requirements first (for layer caching)
COPY requirements.txt .

# 📦 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🗂️ Copy the rest of the codebase
COPY . .

# 🌐 UTF-8 Encoding settings (avoid Unicode issues)
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 🔐 Copy environment variables file
COPY .env.production .env.production

# 🚀 Copy and prepare startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# 🌍 Expose FastAPI default port
EXPOSE 8000

# 🚦 Start app using the startup script (runs migrations + uvicorn)
CMD ["/start.sh"]
