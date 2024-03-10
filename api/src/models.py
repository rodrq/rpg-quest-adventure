from sqlalchemy import MetaData
from src.constants import POSTGRES_INDEXES_NAMING_CONVENTION
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)

Base = declarative_base(metadata=metadata)


# characters = Table(
#     "character",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False, unique=True),
#     Column("class_", Enum(CharacterClassEnum), nullable=False),
#     Column("virtue", Enum(CharacterVirtueEnum), nullable=False),
#     Column("flaw", Enum(CharacterFlawEnum), nullable=False),
#     Column("honor_points", Integer, default=0),
#     Column("char_state", Enum(CharacterStateEnum), default=CharacterStateEnum.adventuring),
#     Column("map_level", Integer, default=1),
#     Column("times_reset", Integer, default=0),
#     Column("created_at", DateTime, server_default=func.now(), nullable=False),
#     Column("role", Enum(UserRoleEnum), default=UserRoleEnum.user))

# quests = Table(
#     "quest",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String),
#     Column("description", String),
#     Column("character_username", String, ForeignKey('characters.username')),
#     Column("cost", Float),
#     Column("approaches", JSON),
#     Column("selected_approach", Integer, default=None),
#     Column("survived", Boolean, default=None),
#     Column("created_at", DateTime, server_default=func.now(), nullable=False)
# )