from src.config import settings

class AuthConfig():
    JWT_ALG: str = "HS256"
    JWT_SECRET: str = settings.JWT_SECRET
    JWT_EXP: int = 24  # hours


auth_config = AuthConfig()
