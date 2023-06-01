from src.models.BaseModel import Base, Dictable
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from src.schemas.User.CreateUseSchema import CreateUserSchema


class UserModel(Base, Dictable):
    __tablename__ = "t_utilisateur"
    code_utilisateur = Column(Integer, primary_key=True, autoincrement=True)
    nom_utilisateur = Column(String(50), default=None)
    prenom_utilisateur = Column(String(50), default=None)
    username = Column(String(50), default=None)
    couleur_fond_utilisateur = Column(Integer, default=0)
    date_insc_utilisateur = Column(Date)

    @staticmethod
    def create_default(user_to_create: CreateUserSchema):
        new_model = UserModel()
        new_model.username = user_to_create.username
        new_model.nom_utilisateur = user_to_create.nom_utilisateur
        new_model.prenom_utilisateur = user_to_create.prenom_utilisateur
        new_model.couleur_fond_utilisateur = 0
        new_model.date_insc_utilisateur = datetime.now()
        return new_model
