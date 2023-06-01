from fastapi import Depends
from sqlalchemy.orm import Session,lazyload

from src.config import Database
from src.config.Database import get_db_connection
from src.models.ItemModel import ItemModel


class ItemRepository:
    __db: Session

    def __init__(self, db: Session = Depends(get_db_connection)):
        self.__db = db

    def getAll(self):
        """
        Returns every entity
        :return: every entity
        """
        return self.__db.query(ItemModel).all()

    def getOne(self,codeobj:int) -> ItemModel:
        """
        get an entity by id
        :param codeobj: id ot the item te get
        :return: object with the id 'codeobj'
        """
        return self.__db.get(ItemModel,codeobj)



    def create(self, item: ItemModel) -> ItemModel:
        """
        inserts a new entity into the database
        :param item: new item to insert
        :return: item added into the database
        """
        self.__db.add(item)
        self.__db.commit()
        self.__db.refresh(item)
        return item

    def update(self, codeobj: int, item: ItemModel) -> ItemModel:
        """
        updates an entity in the database
        :param codeobj: id of the item to edit
        :param item: new values for the item
        :return: edited item
        """
        self.__db.query(ItemModel).filter_by(codeobj=codeobj).update(item.to_dict_none_safe())
        self.__db.commit()
        self.__db.refresh(item)
        return item

    def delete(self, codeobj:int) -> None:
        """
        deletes the item with the id 'codeobj'
        :param codeobj: id of the entity to delete
        """
        itemToDelete:ItemModel = self.getOne(codeobj)
        self.__db.delete(itemToDelete)
        self.__db.commit()
