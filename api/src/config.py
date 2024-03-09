from pydantic import AnyUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict



# First reads env vars, then .env, then default or raises error
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.local", env_file_encoding="utf-8")
    
    OPENAI_API_KEY: str
    OPENAI_ORG_ID: str
    DB_URL: str
    HASH_SECRET_KEY: str
    ALLOWED_CORS_ORIGINS: set[AnyUrl]
    ENVIRONMENT: str


app_configs = {"title": "RPG Quest API"}

if Settings().ENVIRONMENT != "local":
    # If not on local hides /docs
    app_configs["openapi_url"] = None
    