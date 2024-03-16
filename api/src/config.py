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


def get_conn_str():
    return f"""
    dbname={settings.POSTGRES_DB}
    user={settings.POSTGRES_USER}
    password={settings.POSTGRES_PASSWORD}
    host={settings.POSTGRES_HOST}
    port={settings.POSTGRES_PORT}
    """


app_configs = {
    "title": "RPG Quest API",
    "openapi_url": "/docs",
}


if settings.ENVIRONMENT != "local":
    # If not on local hides /docs
    app_configs["openapi_url"] = None  # type: ignore
