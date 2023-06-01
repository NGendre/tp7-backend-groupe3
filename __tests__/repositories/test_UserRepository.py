from unittest import TestCase
from unittest.mock import MagicMock
from src.models.UserModel import UserModel
from src.repositories.UserRepository import UserRepository


class TestUserRepository(TestCase):

    def setUp(self) -> None:
        self.mock_db = MagicMock()
        self.user_repository = UserRepository(db=self.mock_db)

    def test_create(self):
        user = UserModel()

        user_created = self.user_repository.create(user)

        self.mock_db.add.assert_called_once_with(user)
        self.mock_db.commit.assert_called_once()
        self.mock_db.refresh.assert_called_once_with(user)
        self.assertEqual(user_created, user)

    def test_get_all(self):
        users = [
            UserModel(),
            UserModel(),
            UserModel()
        ]
        self.mock_db.query.return_value.all.return_value = users
        all_users = self.user_repository.get_all()

        self.mock_db.query.assert_called_once_with(UserModel)
        self.mock_db.query.return_value.all.assert_called_once()
        self.assertEqual(all_users, users)

    def test_get_one(self):
        user = UserModel()
        user.code_utilisateur = 1
        self.mock_db.get.return_value = user

        user_in_db = self.user_repository.get_one(user.code_utilisateur)

        self.mock_db.get.assert_called_once_with(UserModel, user.code_utilisateur)
        self.assertEqual(user_in_db, user)

    def test_update_one(self):
        user = UserModel()
        user.code_utilisateur = 1
        self.mock_db.query.return_value.filter_by.return_value.update.return_value = user
        self.user_repository.get_one = MagicMock()
        self.user_repository.get_one.return_value = user

        user_in_db = self.user_repository.update_one(user.code_utilisateur, user)

        self.mock_db.query.assert_called_once_with(UserModel)
        self.mock_db.query.return_value.filter_by.assert_called_once_with(code_utilisateur=user.code_utilisateur)
        self.mock_db.query.return_value.filter_by.return_value.update.assert_called_once_with(user.to_dict_none_safe())
        self.mock_db.commit.assert_called_once()
        self.user_repository.get_one.assert_called_once_with(user.code_utilisateur)
        self.assertEqual(user_in_db, user)

    def test_delete(self):
        user = UserModel()
        user.code_utilisateur = 1

        self.user_repository.delete(user.code_utilisateur)

        self.mock_db.query.assert_called_once_with(UserModel)
        self.mock_db.query.return_value.filter_by.assert_called_once_with(code_utilisateur=user.code_utilisateur)
        self.mock_db.query.return_value.filter_by.return_value.delete.assert_called_once()
        self.mock_db.commit.assert_called_once()
        self.mock_db.flush.assert_called_once()
