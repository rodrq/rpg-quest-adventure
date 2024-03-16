from pydantic import AnyUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


# First reads env vars, then .env, then default or raises error
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.local", env_file_encoding="utf-8")

    GEMINI_API_KEY: str

    ALLOWED_CORS_ORIGINS: set[AnyUrl]
    ENVIRONMENT: str

    JWT_SECRET: str

    DB_URL: PostgresDsn
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int


settings = Settings()


app_configs = {
    "title": "RPG Quest API",
    "openapi_url": "/docs",
}


if settings.ENVIRONMENT != "local":
    # If not on local hides /docs
    app_configs["openapi_url"] = None  # type: ignore
