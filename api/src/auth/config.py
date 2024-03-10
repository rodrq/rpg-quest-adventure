from src.config import settings

class AuthConfig():
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = settings.JWT_SECRET
    JWT_EXP: int = 5  # minutes

    REFRESH_TOKEN_KEY: str = "refreshToken"
    REFRESH_TOKEN_EXP: int = 60 * 60 * 24 * 14


auth_config = AuthConfig()
