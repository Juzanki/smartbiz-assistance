# ✅ Base image
FROM python:3.10-slim

# ✅ Set workdir
WORKDIR /app

# ✅ Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy everything else
COPY . .

# ✅ Expose port (Railway uses env PORT)
EXPOSE 8000

# ✅ Run using start.py
CMD ["python", "start.py"]
