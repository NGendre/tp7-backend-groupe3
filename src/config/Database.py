from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from src.config.env_config import database_url, database_name, database_password, database_user


SQLALCHEMY_DATABASE_URL = f"mysql://{database_user}:{database_password}@{database_url}/{database_name}"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)


Base = declarative_base()


SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
