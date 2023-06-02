from fastapi import APIRouter, Body, Depends, HTTPException, status

from src.schemas.User.CreateUseSchema import CreateUserSchema
from src.schemas.User.UpdateUserSchema import UpdateUserSchema
from src.schemas.User.UserSchema import UserSchema
from src.services.UserService import UserService

UsersRouter = APIRouter(
    prefix="/users", tags=["admin"]
)


def handle_user_found(user: UserSchema) -> None:
    """
    Function to verify if user is set. If it is, this function does nothing.
    If it is set to None it will raise an :class:`fastapi.HTTPException` with error code 404 and message "User not found"
    :param user: User to verify
    :type user: UserSchema
    :raises HTTPException: HTTPException 404 for user not found.
    """
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")


@UsersRouter.post("/", status_code=status.HTTP_201_CREATED, response_model=UserSchema)
def create_user(user: CreateUserSchema = Body(), user_service: UserService = Depends()) -> UserSchema:
    """
    POST Endpoint for creating a new User.
    :<b>param</b> user: Schema validation to send in body request <br>
    :type user: CreateUserSchema <br>
    :param user_service: User Service Instance, given by Dependency Injection <br>
    :type user_service: UserService <br>
    :return: The new User created <br>
    :rtype: UserSchema
    """
    user_created = user_service.create_user(user)
    return user_created


@UsersRouter.get("/", response_model=list[UserSchema])
def get_all_users(user_service: UserService = Depends()) -> list[UserSchema]:
    """
    GET Endpoint for getting all Users
    :param user_service: User Service Instance, given by Dependency Injection
    :type user_service: UserService
    :return: List of all Users
    :rtype: list[UserSchema]
    """
    return user_service.get_all_users()


@UsersRouter.get("/{id}", response_model=UserSchema)
def get_user(id: int, user_service: UserService = Depends()) -> UserSchema | HTTPException:
    """
    GET Endpoint for getting one User by his ID
    :param id: ID of the user to find given in path parameter
    :type id: int
    :param user_service: User Service Instance, given by Dependency Injection
    :type user_service: UserService
    :return: User found with ID given
    :rtype: UserSchema
    """
    user_found = user_service.get_user_by_id(id)
    handle_user_found(user_found)
    return user_found


@UsersRouter.patch("/{id}", response_model=UserSchema)
def update_user(id: int, user: UpdateUserSchema, user_service: UserService = Depends()) -> UserSchema | HTTPException:
    """
    PATCH Endpoint to update a user by his ID
    :param id: ID of the user to find given in path parameter
    :type id: int
    :param user: Schema validation to send in body request
    :type user: UpdateUserSchema
    :param user_service: User Service Instance, given by Dependency Injection
    :type user_service: UserService
    :return: User modified with ID given
    :rtype: UserSchema
    """
    user_found: UserSchema = user_service.update_one_by_id(id, user)
    handle_user_found(user_found)
    return user_found


@UsersRouter.delete("/{id}", response_model=None)
def delete_user(id: int, user_service: UserService = Depends()) -> None:
    """
    DELETE Endpoint to delete a user by his ID
    param id: ID of the user to find given in path parameter
    :type id: int
    :param user_service: User Service Instance, given by Dependency Injection
    :type user_service: UserService
    """
    user_service.delete_on_by_id(id)
