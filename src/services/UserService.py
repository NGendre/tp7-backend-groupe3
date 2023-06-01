from datetime import datetime

from src.schemas.User.UpdateUserSchema import UpdateUserSchema
from src.schemas.User.UserSchema import UserSchema
from src.schemas.User.UserSchema import CreateUserSchema
from src.repositories.UserRepository import UserRepository
from fastapi import Depends
from src.models.UserModel import UserModel


class UserService:
    """
    UserService is used for managing Users logic
    """
    __user_repository: UserRepository
    """
    UserService has a dependency to work. It has to be set in __init__ method
    """
    def __init__(self, user_repository: UserRepository = Depends()):
        """
        :param user_repository: Class responsable to manage database operations
        :type user_repository: UserRepository
        """
        self.__user_repository = user_repository

    def create_user(self, user: CreateUserSchema):
        """Create a User and save it a database
        :param user: user data validated
        :type user: CreateUserSchema
        :return: The user created
        :rtype: UserModel
        """
        new_user = UserModel.create_default(user)
        new_user_saved = self.__user_repository.create(new_user)
        return UserSchema.from_orm(new_user_saved)

    def get_all_users(self) -> list[UserModel]:
        """
        Instance method to get all Users
        :return: List of all Users
        :rtype: list[UserModel]
        """
        return self.__user_repository.get_all()

    def get_user_by_id(self, id: int) -> UserModel | None:
        """
        Instance method to get one User by his ID
        :param id: ID of the User
        :type id: int
        :return: User if he is found or None if not found
        :rtype: UserModel | None
        """
        return self.__user_repository.get_one(id)

    def update_one_by_id(self, id: int, user: UpdateUserSchema) -> UserModel | None:
        """
        Instance method to update one User by his ID
        :param id: ID of the User
        :type id: int
        :param user: User with his data to update
        :type user: UpdateUserSchema
        :return: User with data updated if he is found or None if not found
        :rtype: UserModel | None
        """
        user_updated = UserModel()
        user_updated.username = user.username
        user_updated.nom_utilisateur = user.nom_utilisateur
        user_updated.prenom_utilisateur = user.prenom_utilisateur
        user_updated.couleur_fond_utilisateur = user.couleur_fond_utilisateur
        return self.__user_repository.update_one(id, user_updated)

    def delete_on_by_id(self, id: int) -> None:
        """
        Instance method to delete one User by his ID

        IMPORTANT:
        Even if User doesn't exist, it does not raise an Exception nor delete another User. It just do nothing.
        :param id: ID of the User
        :type id: int
        """
        self.__user_repository.delete(id)
