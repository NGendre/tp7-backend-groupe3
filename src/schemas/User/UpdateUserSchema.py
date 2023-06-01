from typing import Optional
from pydantic import BaseModel


class UpdateUserSchema(BaseModel):
    """
    Pydantic Schema for update a User
    """
    couleur_fond_utilisateur: Optional[int]
    nom_utilisateur: Optional[str]
    prenom_utilisateur: Optional[str]
    username: Optional[str]
