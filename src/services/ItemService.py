from src.models.ItemModel import ItemModel
from src.repositories.ItemRepository import ItemRepository
from fastapi import Depends

from src.schemas import ItemSchema


class ItemService:
    _itemRepository = ItemRepository

    def __init__(self,itemRepository: ItemRepository = Depends()):
        self._itemRepository = itemRepository

    def getAll(self) -> ItemModel:
        """
        retrieves result from the getAll method in the repository
        :return: all item entities
        """
        return self._itemRepository.getAll()

    def getOne(self,codeobj) -> ItemModel:
        """
        retrieves result from getOne method in repository, with a given ID
        :param codeobj: ID of the item to retrieve
        :return: item with corresponding id
        """
        return self._itemRepository.getOne(codeobj)


    def create(self, item: ItemSchema) -> ItemModel:
        """
        sends a new entity to the repository
        :param item: new item
        :return: new item transformet with necessary data only
        """
        return self._itemRepository.create(ItemModel.CreateItemModelFromSchema(item))


    def update(self, codeobj: int, item: ItemSchema) -> ItemModel:
        """
        sends dqtq and an id to update an entity
        :param codeobj: id of the entity to update
        :param item: item with new values
        :return: updated entity with new values
        """
        return self._itemRepository.update(codeobj,ItemModel.CreateItemModelFromSchema(item))

    def delete(self, codeobj: int) -> None:
        """
        Sends the id of an entity to be deletedby the repository
        :param codeobj: id of the item to delete
        """
        self._itemRepository.delete(codeobj)



