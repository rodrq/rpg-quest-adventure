from openai import OpenAI
from src.config.settings import OPENAI_API_KEY, OPENAI_ORG_ID

openai_client = OpenAI(api_key=OPENAI_API_KEY, organization = OPENAI_ORG_ID)
