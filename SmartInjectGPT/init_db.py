import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Ongeza root ya SmartBiz_Assistance kwenye sys.path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# ✅ Badili import kuwa na prefix ya SmartInjectGPT
try:
    from SmartInjectGPT.backend.db import Base
    import SmartInjectGPT.backend.models.user
    import SmartInjectGPT.backend.models.dream_log
except ModuleNotFoundError as e:
    print(f"❌ Module import error: {e}")
    print("💡 Hakikisha jina na path ni sahihi.")
    sys.exit(1)

# Load env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("❌ DATABASE_URL haijapatikana kwenye .env file.")
    sys.exit(1)

# Create tables
print("🔧 Creating tables...")
try:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")
except SQLAlchemyError as e:
    print(f"❌ Error creating tables: {e}")
    sys.exit(1)
