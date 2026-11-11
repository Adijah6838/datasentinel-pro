from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "DataSentinel Pro"
    ENVIRONMENT: str = "development"
    API_V1_PREFIX: str = "/api/v1"
    
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    CREDENTIALS_ENCRYPTION_KEY: str

settings = Settings()
