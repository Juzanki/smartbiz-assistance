# ================================================================
# ⚙️ Alembic Migration Environment Setup
# ✅ SmartBiz Assistance — Railway & Local Support
# 📦 Loads config from .env.production (RAILWAY_DATABASE_URL)
# ================================================================

import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# ==================== 📂 Load Environment =========================
# Load environment variables from .env.production in parent folder
base_dir = os.path.dirname(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(base_dir, ".env.production"))

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
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
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
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
