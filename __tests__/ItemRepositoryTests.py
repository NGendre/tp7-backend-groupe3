import unittest
from unittest.mock import MagicMock
from src.models.ItemModel import ItemModel
from src.repositories.ItemRepository import ItemRepository

class ItemRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.db_session_mock = MagicMock()
        self.item_repository = ItemRepository(db=self.db_session_mock)

    def test_get_all(self):
        # Mocking the query result
        items = [ItemModel(libobj='Item 1'), ItemModel(libobj='Item 2')]
        self.db_session_mock.query.return_value.all.return_value = items
        result = self.item_repository.getAll()
        self.assertEqual(result, items)
        self.db_session_mock.query.assert_called_once_with(ItemModel)
        self.db_session_mock.query.return_value.all.assert_called_once()

    def test_get_one(self):
        libobj = 1
        item = ItemModel(libobj='Item 1')
        self.db_session_mock.get.return_value = item
        result = self.item_repository.getOne(libobj)
        self.assertEqual(result, item)
        self.db_session_mock.get.assert_called_once_with(ItemModel, libobj)

    def test_create(self):
        item = ItemModel(libobj='New Item')
        self.item_repository.create(item)

        self.db_session_mock.add.assert_called_once_with(item)
        self.db_session_mock.commit.assert_called_once()
        self.db_session_mock.refresh.assert_called_once_with(item)

    def test_update(self):
        codeobj = 1
        item = ItemModel(libobj='Updated Item')
        self.item_repository.update(codeobj, item)

        self.db_session_mock.query.assert_called_once_with(ItemModel)
        self.db_session_mock.query.return_value.filter_by.assert_called_once_with(codeobj=codeobj)
        self.db_session_mock.query.return_value.filter_by.return_value.update.assert_called_once_with(item.to_dict_none_safe())
        self.db_session_mock.commit.assert_called_once()
        self.db_session_mock.refresh.assert_called_once_with(item)

    def test_delete(self):
        libobj = 1
        item = ItemModel(libobj='Item 1')
        self.item_repository.getOne = MagicMock(return_value=item)

        self.item_repository.delete(libobj)

        self.item_repository.getOne.assert_called_once_with(libobj)
        self.db_session_mock.delete.assert_called_once_with(item)
        self.db_session_mock.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()