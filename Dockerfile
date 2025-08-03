# 🐍 Base Python image (lightweight + secure)
FROM python:3.10-slim

# 📁 Set working directory inside the container
WORKDIR /app

# 🔧 Install essential build tools (for psycopg2, wheel, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 📦 Copy dependencies first for Docker caching
COPY requirements.txt .

# 🧪 Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 📁 Copy full source code
COPY . .

# 🌐 Expose port (Railway injects $PORT, fallback is 8000)
EXPOSE 8000

# 🚀 Run FastAPI app using uvicorn (production entrypoint)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
