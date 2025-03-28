from sqlmodel import SQLModel, Session
from .config import DATABASE_URL, DB_TIMEZONE
import sqlmodel

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL is not set")


engine = sqlmodel.create_engine(
    DATABASE_URL,  pool_pre_ping=True
)


def init_db():
    print("creating database")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
