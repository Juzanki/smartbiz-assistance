# ✅ Base Python image (lightweight + secure)
FROM python:3.10-slim

# ✅ Set working directory inside the container
WORKDIR /app

# ✅ Install essential system packages (e.g., for psycopg2, wheels)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Copy requirements file first for Docker layer caching
COPY requirements.txt .

# ✅ Install Python dependencies safely
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the rest of the application code into container
COPY . .

# ✅ Expose port (Railway injects $PORT; fallback to 8000)
EXPOSE 8000

# ✅ Launch FastAPI with Uvicorn (production-safe)
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
