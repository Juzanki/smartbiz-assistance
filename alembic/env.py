# === 📂 env.py - Alembic Migration Entrypoint ===
import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# === 🔐 Load environment variables from .env.production ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(BASE_DIR, '.env.production'))

# === 🛠️ Add project root (backend) to Python path ===
sys.path.append(BASE_DIR)

# === 🧱 Import SQLAlchemy Base and models ===
from backend.db import Base  # Make sure Base = declarative_base()
from backend.models import *  # Import all models (they must be exposed via __init__.py)

# === 🔧 Alembic Config Setup ===
config = context.config
config_file = config.config_file_name

# ✅ Set DB URL from env dynamically
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ✅ Configure logging
if config_file is not None:
    fileConfig(config_file)

# === 🧠 Metadata from SQLAlchemy Base ===
target_metadata = Base.metadata

# === 📝 Offline migrations (e.g., generate SQL without DB) ===
def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# === 🛠️ Online migrations (apply directly to DB) ===
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Detect column type changes
            compare_server_default=True,  # Detect default changes
        )

        with context.begin_transaction():
            context.run_migrations()

# === 🚦 Entry point ===
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
