<<<<<<< HEAD
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
=======
# ================================================================
# ⚙️ Alembic Migration Environment Setup
# ✅ SmartBiz Assistance — Railway & Local Support
# 📦 Loads config from .env.production (RAILWAY_DATABASE_URL)
# ================================================================

import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ==================== 📂 Load Environment =========================
# Load environment variables from .env.production in parent folder
base_dir = os.path.dirname(os.path.dirname(__file__))

# Fetch the database URL from environment
DATABASE_URL = os.getenv("RAILWAY_DATABASE_URL")

# ==================== ⚙️ Alembic Config ==========================
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ==================== 🧠 Metadata (Models) ========================
# If using SQLAlchemy models, import Base.metadata here
# from backend.models import Base
target_metadata = None  # Set to Base.metadata if needed

# ==================== 🔁 Migration Modes ==========================

def run_migrations_offline() -> None:
    """Run migrations without a DB connection — outputs SQL statements."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
>>>>>>> 39aaa5419d4d78972badb2e9bf74eb1ffebb8a0d
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
<<<<<<< HEAD

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
=======
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations with an active DB connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


# ==================== 🚀 Entry Point =============================
>>>>>>> 39aaa5419d4d78972badb2e9bf74eb1ffebb8a0d
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
