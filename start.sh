#!/bin/bash

echo "Loading environment..."
export $(grep -v '^#' .env.production | xargs)

echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting FastAPI app..."
exec uvicorn backend.main:app --host=0.0.0.0 --port=8000
