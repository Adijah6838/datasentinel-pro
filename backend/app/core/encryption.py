from cryptography.fernet import Fernet
from app.core.config import settings

# We use the key from our .env file
fernet = Fernet(settings.CREDENTIALS_ENCRYPTION_KEY.encode())

def encrypt_credentials(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_credentials(encrypted_data: str) -> str:
    return fernet.decrypt(encrypted_data.encode()).decode()