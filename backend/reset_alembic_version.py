# backend/reset_alembic_version.py
from sqlalchemy import text
from backend.db import engine

with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
    conn.commit()

print("✅ Alembic version table dropped successfully.")
