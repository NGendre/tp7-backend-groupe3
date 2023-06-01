from datetime import datetime

from unittest import TestCase
from unittest.mock import MagicMock
from fastapi import HTTPException, status

from src.routers.admin.users.AdminUserRouter import create_user, get_all_users, get_user, update_user, delete_user, \
    handle_user_found
from src.schemas.User.CreateUseSchema import CreateUserSchema
from src.schemas.User.UpdateUserSchema import UpdateUserSchema
from src.schemas.User.UserSchema import UserSchema
from src.services.UserService import UserService


class TestAdminUserRouter(TestCase):

    def setUp(self) -> None:
        self.user_service_mock = MagicMock(spec=UserService)
        self.user_schema_mock = UserSchema(code_utilisateur=1, username="test_user",
                                           prenom_utilisateur="John", nom_utilisateur="Doe",
                                           couleur_fond_utilisateur=0, date_insc_utilisateur=datetime.now())

    def test_create_user(self):
        create_user_schema = CreateUserSchema(username="test_user", prenom_utilisateur="John", nom_utilisateur="Doe")
        self.user_service_mock.create_user.return_value = self.user_schema_mock

        create_user_response = create_user(user=create_user_schema, user_service=self.user_service_mock)

        self.user_service_mock.create_user.assert_called_once_with(create_user_schema)
        self.assertEqual(create_user_response, self.user_schema_mock)

    def test_get_all_users(self):
        self.user_service_mock.get_all_users.return_value = [self.user_schema_mock]

        get_all_users_response = get_all_users(user_service=self.user_service_mock)

        self.assertEqual(get_all_users_response, [self.user_schema_mock])
        self.user_service_mock.get_all_users.assert_called_once()

    def test_get_user_found(self):
        self.user_service_mock.get_user_by_id.return_value = self.user_schema_mock

        get_user_response = get_user(id=1, user_service=self.user_service_mock)

        self.user_service_mock.get_user_by_id.assert_called_once_with(1)
        self.assertEqual(get_user_response, self.user_schema_mock)

    def test_get_user_not_found(self):
        self.user_service_mock.get_user_by_id.return_value = None

        with self.assertRaises(HTTPException) as context:
            get_user(id=1, user_service=self.user_service_mock)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "User not found")
        self.user_service_mock.get_user_by_id.assert_called_once_with(1)

    def test_update_user_found(self):
        user_update_schema_mock = UpdateUserSchema()
        user_schema_mock = self.user_schema_mock
        self.user_service_mock.update_one_by_id.return_value = user_schema_mock

        update_user_response = update_user(id=1, user=user_update_schema_mock, user_service=self.user_service_mock)

        self.assertEqual(update_user_response, user_schema_mock)
        self.user_service_mock.update_one_by_id.assert_called_once_with(1, user_update_schema_mock)

    def test_update_user_not_found(self):
        self.user_service_mock.update_one_by_id.return_value = None
        user_update_schema_mock = UpdateUserSchema()

        with self.assertRaises(HTTPException) as context:
            update_user(id=1, user=user_update_schema_mock, user_service=self.user_service_mock)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "User not found")
        self.user_service_mock.update_one_by_id.assert_called_once_with(1, user_update_schema_mock)

    def test_delete_user(self):
        delete_user(id=1, user_service=self.user_service_mock)

        self.user_service_mock.delete_on_by_id.assert_called_once_with(1)

    def test_handle_user_not_found(self):
        with self.assertRaises(HTTPException) as context:
            handle_user_found(None)

        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(context.exception.detail, "User not found")

    def test_handle_user_found(self):
        user_schema_mock = self.user_schema_mock

        result =  handle_user_found(user_schema_mock)

        self.assertIsNone(result)
