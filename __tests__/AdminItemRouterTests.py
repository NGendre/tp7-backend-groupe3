import unittest
from unittest.mock import MagicMock
from src.models.ItemModel import ItemModel
from src.routers.admin.items.AdminItemRouter import addItem, updateOne
from src.schemas.ItemSchema import ItemSchema
from src.services.ItemService import ItemService


class ItemRouterTests(unittest.TestCase):
    def setUp(self):
        self.item_service_mock = MagicMock(spec=ItemService)
        self.item_schema = ItemSchema(libobj = 'test',tailleobj = 'grand',puobj = 11.1,poidsobj = 22.2)

    def test_add_item(self):
        self.item_service_mock.addItem.return_value = self.item_schema
        addOneUser = addItem(self.item_schema,self.item_service_mock)
        self.item_service_mock.assert_called_once_with(self.item_schema)
        self.assertEquals(self.item_schema,addOneUser)

    def test_get_one(self):
        getOneUser = self.item_service_mock.getOne(item_service_mock=self.item_service_mock)
        self.assertEquals(getOneUser, self.item_schema)
        self.item_service_mock.assert_called_once()

    def test_get_all(self):
        getAllUsers = self.item_service_mock.getAll(item_service_mock = self.item_service_mock)
        self.assertEquals(getAllUsers,self.item_schema)
        self.item_service_mock.assert_called_once()

    def test_update_one(self):
        self.item_service_mock.update.return_value = self.item_schema
        updateOneUser = updateOne(self.item_schema,self.item_service_mock)
        self.item_service_mock.assert_called_once_with(self.item_schema)
        self.assertEquals(self.item_schema,updateOneUser)


    def test_delete_one(self):
        ItemService.delete(1)
        self.item_service_mock.delete.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
