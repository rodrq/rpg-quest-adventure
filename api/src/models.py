from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from src.constants import POSTGRES_INDEXES_NAMING_CONVENTION

metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)

Base = declarative_base(metadata=metadata)
