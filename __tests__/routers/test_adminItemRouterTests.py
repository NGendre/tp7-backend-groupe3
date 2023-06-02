import unittest
from unittest.mock import MagicMock

from src.routers.admin.items.AdminItemRouter import addItem, deleteOne, getAll, getOne, updateOne
from src.schemas.ItemSchema import ItemSchema
from src.services.ItemService import ItemService


class ItemRouterTests(unittest.TestCase):
    def setUp(self):
        self.item_service_mock = MagicMock(spec=ItemService)
        self.item_schema = ItemSchema(libobj='test', tailleobj='grand', puobj=11.1, poidsobj=22.2)

    def test_add_item(self):
        self.item_service_mock.create.return_value = self.item_schema
        addOneUser = addItem(self.item_schema, self.item_service_mock)
        self.item_service_mock.create.assert_called_once_with(self.item_schema)
        self.assertEqual(self.item_schema, addOneUser)

    def test_get_one(self):
        self.item_service_mock.getOne.return_value = self.item_schema
        getOneUser = getOne(1, self.item_service_mock)
        self.assertEqual(getOneUser, self.item_schema)
        self.item_service_mock.getOne.assert_called_once_with(1)

    def test_get_all(self):
        self.item_service_mock.getAll.return_value = self.item_schema
        getAllUsers = getAll(self.item_service_mock)
        self.assertEqual(getAllUsers, self.item_schema)
        self.item_service_mock.getAll.assert_called_once()

    def test_update_one(self):
        self.item_service_mock.update.return_value = self.item_schema
        updateOneUser = updateOne(1, self.item_schema, self.item_service_mock)
        self.item_service_mock.update.assert_called_once_with(1, self.item_schema)
        self.assertEqual(self.item_schema, updateOneUser)

    def test_delete_one(self):
        deleteOne(1, self.item_service_mock)
        self.item_service_mock.delete.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
