from src.config.Database import get_db_connection
from fastapi import Depends
from src.models.UserModel import UserModel
from sqlalchemy.orm import Session


class UserRepository:
    """
    UserRepository is used for managing database operations for Users Entities
    """
    __db: Session
    """
    Private attribute of UserRepository instance.
    UserRepository has a dependency to work. It has to be set in __init__ method.
    """
    def __init__(self, db: Session = Depends(get_db_connection)):
        """
        :param db: Connexion Session to the database
        :type db: Session
        """
        self.__db = db

    def create(self, user: UserModel) -> UserModel:
        """
        Save a User in the database.
        :param user: User To save.
        :type user: UserModel
        :return: User saved in the database.
        :rtype: UserModel
        """
        self.__db.add(user)
        self.__db.commit()
        self.__db.refresh(user)
        return user

    def get_all(self) -> list[UserModel]:
        """
        Gets all Users in the database.
        :return: List of Users in the database.
        :rtype: list[UserModel]
        """
        return self.__db.query(UserModel).all()

    def get_one(self, id: int) -> UserModel | None:
        """
        Get one User in the database by his ID.
        :param id: ID of the User.
        :return: User if he is found in the database or None if not found
        :rtype: UserModel | None
        """
        return self.__db.get(UserModel, id)

    def update_one(self, id: int, user: UserModel) -> UserModel | None:
        """
        Find User in the database by his ID then updates all values needed.
        :param id: ID of the User.
        :type id: int
        :param user: User with updated data.
        :type user: UserModel
        :return: User with updated data if he is found in the database or None if not found
        :rtype: UserModel | None
        """
        self.__db\
            .query(UserModel)\
            .filter_by(code_utilisateur=id)\
            .update(user.to_dict_none_safe())
        self.__db.commit()
        return self.get_one(id)

    def delete(self, id: int) -> None:
        """
        Delete User in the database by his ID.
        :param id: ID of the User.
        :type id: int
        """
        self.__db.query(UserModel).filter_by(code_utilisateur=id).delete()
        self.__db.commit()
        self.__db.flush()
