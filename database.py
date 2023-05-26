# Justine - 12122022 - V1

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env_config import database_url, database_name, database_password, database_user

# connexion a la base de donnée et déclaration de la base avec sql alchemy

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = f"mysql://{database_user}:{database_password}@{database_url}/{database_name}"


# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()

# creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

