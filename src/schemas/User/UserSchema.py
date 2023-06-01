import datetime

from src.schemas.User.CreateUseSchema import CreateUserSchema


class UserSchema(CreateUserSchema):
    """
    Pydantic Schema for a complete User
    """
    date_insc_utilisateur: datetime.date
    code_utilisateur: int
    couleur_fond_utilisateur: int

    class Config:
        orm_mode = True
