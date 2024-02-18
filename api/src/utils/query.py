from sqlalchemy.orm import Session
from src.config.database import engine
from sqlalchemy import func
from src.models.models import Character

def db_query_value(table, column, value):
    with Session(engine) as session:
            queried_value = session.query(table).filter(column == value).first()
            return queried_value
            
def get_character(username: str):
    with Session(engine) as session:
            queried_character = session.query(Character).filter(func.lower(Character.username) == username.lower()).first()
            return queried_character