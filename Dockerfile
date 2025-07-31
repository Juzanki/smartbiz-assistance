# ====================================================
# ✅ Dockerfile for SmartBiz Assistance (Fixed PORT error)
# ====================================================

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

EXPOSE 8000

# ✅ Launch via start.py to use dynamic PORT
CMD ["python", "backend/start.py"]
