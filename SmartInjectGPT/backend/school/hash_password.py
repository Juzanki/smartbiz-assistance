from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

if __name__ == "__main__":
    plain_password = input("🔑 Enter password to hash: ")
    hashed = hash_password(plain_password)
    print("\n🔐 Your Hashed Password:\n", hashed)
