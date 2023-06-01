from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    """
    Pydantic Schema for create a User
    """
    nom_utilisateur: str
    prenom_utilisateur: str
    username: str
