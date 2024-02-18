from starlette.config import Config

#First reads env vars, then .env, then default or raises error
config = Config('.env')

DB_URL = config('DB_URL')
OPENAI_API_KEY = config('OPENAI_API_KEY')
OPENAI_ORG_ID = config('OPENAI_ORG_ID')
SECRET_KEY=config('SECRET_KEY')
ALGORITHM=config('ALGORITHM')
TOKEN_LIFETIME_MINUTES=config('TOKEN_LIFETIME_MINUTES')
CORS_ORIGINS=config('CORS_ORIGINS')
