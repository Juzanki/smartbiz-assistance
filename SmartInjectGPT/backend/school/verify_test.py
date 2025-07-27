from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

hashed = "$2b$12$mXP7hKVGWaIpyg0GJU1FvO/q8LQEpepIu9mP7tW4ZD/xyKMsTtd0u"  # ← password_hash kutoka DB
plain = "1Juzanki@01@"  # ← password uliyoandika wakati wa login

is_valid = pwd_context.verify(plain, hashed)

print("✅ Password Match!" if is_valid else "❌ Password NOT matching")
