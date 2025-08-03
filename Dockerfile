# ✅ Dockerfile for SmartBiz Assistance backend (Railway Ready)

# 🐍 Base Python image
FROM python:3.10-slim

# 🗂️ Set working directory
WORKDIR /app

# ⚙️ Install required system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# 📥 Copy requirements file and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 📦 Copy full project
COPY . .

# 🌐 Set UTF-8 encoding
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 🚪 Expose port (used by Railway)
EXPOSE ${PORT}

# 🚀 Launch Uvicorn app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
