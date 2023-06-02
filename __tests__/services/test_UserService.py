from datetime import datetime
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.models.UserModel import UserModel
from src.schemas.User.CreateUseSchema import CreateUserSchema
from src.schemas.User.UpdateUserSchema import UpdateUserSchema
from src.schemas.User.UserSchema import UserSchema
from src.services.UserService import UserService


class TestUserService(TestCase):

    def setUp(self) -> None:
        self.user_repository = MagicMock()
        self.user_service = UserService(user_repository=self.user_repository)

    def test_create_user(self):
        user_data = CreateUserSchema(username='john_doe', nom_utilisateur='Doe', prenom_utilisateur='John')
        fake_model = UserModel()

        with patch('src.schemas.User.UserSchema.UserSchema.from_orm',
                   return_value=UserSchema(code_utilisateur=1,
                                           username=user_data.username,
                                           nom_utilisateur=user_data.nom_utilisateur,
                                           prenom_utilisateur=user_data.prenom_utilisateur,
                                           couleur_fond_utilisateur=0,
                                           date_insc_utilisateur=datetime.now())):
            with patch('src.models.UserModel.UserModel.create_default', return_value=fake_model):
                self.user_service.create_user(user_data)
        self.user_repository.create.assert_called_once_with(fake_model)

    def test_get_all_users(self):
        user_model_mock1 = MagicMock(spec=UserModel)
        user_model_mock2 = MagicMock(spec=UserModel)
        self.user_repository.get_all.return_value = [user_model_mock1, user_model_mock2]

        result = self.user_service.get_all_users()

        self.user_repository.get_all.assert_called_once()
        self.assertEqual(result, [user_model_mock1, user_model_mock2])

    def test_get_user_by_id(self):
        user_model_mock = MagicMock(spec=UserModel)
        self.user_repository.get_one.return_value = user_model_mock
        user_id = 1

        result = self.user_service.get_user_by_id(user_id)

        self.user_repository.get_one.assert_called_once_with(user_id)
        self.assertEqual(result, user_model_mock)

    def test_update_one_by_id(self):
        user_data = UpdateUserSchema(username='john_doe', nom_utilisateur='Doe', prenom_utilisateur='John')
        user_model_mock = MagicMock(spec=UserModel)
        self.user_repository.update_one.return_value = user_model_mock
        user_id = 1
        user_model_mock.username = user_data.username
        user_model_mock.nom_utilisateur = user_data.nom_utilisateur
        user_model_mock.prenom_utilisateur = user_data.prenom_utilisateur

        result = self.user_service.update_one_by_id(user_id, user_data)

        self.user_repository.update_one.assert_called_once()
        self.assertEqual(result, user_model_mock)

    def test_delete_on_by_id(self):
        user_id = 1

        self.user_service.delete_on_by_id(user_id)

        self.user_repository.delete.assert_called_once_with(user_id)
