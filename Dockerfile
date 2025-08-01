# ✅ Base image
FROM python:3.10-slim

# ✅ Set working directory inside the container
WORKDIR /app

# ✅ Optional system dependencies (for psycopg2 or wheels)
RUN apt-get update && apt-get install -y build-essential gcc

# ✅ Copy only requirements file first for cache optimization
COPY requirements.txt .

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the rest of the application code
COPY . .

# ✅ Expose the port (Railway injects $PORT but defaults to 8000)
EXPOSE 8000

# ✅ Run FastAPI using uvicorn with correct path to main.py
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
