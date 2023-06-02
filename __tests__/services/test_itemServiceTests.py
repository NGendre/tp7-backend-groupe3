import unittest
from unittest.mock import MagicMock,patch
from src.models.ItemModel import ItemModel
from src.repositories.ItemRepository import ItemRepository
from src.services.ItemService import ItemService
from src.schemas.ItemSchema import ItemSchema

class ItemServiceTests(unittest.TestCase):
    def setUp(self):
        self.item_repository_mock = MagicMock(spec=ItemRepository)
        self.item_service = ItemService(itemRepository=self.item_repository_mock)

    def test_get_all(self):
        items = [ItemModel(libobj='Item 1'), ItemModel(libobj='Item 2')]
        self.item_repository_mock.getAll.return_value = items

        result = self.item_service.getAll()

        self.assertEqual(result, items)
        self.item_repository_mock.getAll.assert_called_once()

    def test_get_one(self):
        codeobj = 1
        item = ItemModel(libobj='Item 1')
        self.item_repository_mock.getOne.return_value = item

        result = self.item_service.getOne(codeobj)

        self.assertEqual(result, item)
        self.item_repository_mock.getOne.assert_called_once_with(codeobj)

    def test_create(self):
        item_schema = ItemSchema()
        item_model = ItemModel()
        with patch('src.models.ItemModel.ItemModel.createItemModelFromSchema',return_value=item_model):
            self.item_service.create(item_schema)
        self.item_repository_mock.create.assert_called_once_with(item_model)

    def test_update(self):
        item_schema = ItemSchema()
        item_model = ItemModel()
        with patch('src.models.ItemModel.ItemModel.createItemModelFromSchema', return_value=item_model):
            self.item_service.update(0,item_schema)
        self.item_repository_mock.update.assert_called_once_with(0,item_model)
    def test_delete(self):
        codeobj = 1
        self.item_service.delete(codeobj)
        self.item_repository_mock.delete.assert_called_once_with(codeobj)

if __name__ == '__main__':
    unittest.main()