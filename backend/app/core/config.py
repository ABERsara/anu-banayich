from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    PROJECT_NAME: str = "Practicum Web"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "dev-secret-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    DATABASE_URL: str = "sqlite:///./dev.db"

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost:4200",
        "http://localhost:3000",
    ]


settings = Settings()
