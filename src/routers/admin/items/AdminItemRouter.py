from fastapi import APIRouter,Depends
from starlette import status

from src.schemas.ItemSchema import ItemSchema
from src.services.ItemService import ItemService


ItemRouter = APIRouter(
    prefix='/items'
)



@ItemRouter.post('/', status_code=status.HTTP_201_CREATED)
def addItem(item: ItemSchema,itemService:ItemService = Depends()):
    """
    asks the service to add an entity
    :param item: values of the item in the thhp request body
    :param itemService: Instance of the service being called
    :return: item created
    """
    return itemService.create(item)

@ItemRouter.get('/{codeobj}',status_code=status.HTTP_200_OK)
def getOne(codeobj: int,itemService:ItemService = Depends()):
    """
    requests the service to send an entity with a corrseponding id
    :param codeobj: ID of the item to get, retrieved from the http request param
    :param itemService: Instance of the service being called
    :return: item with corresponding id
    """
    return itemService.getOne(codeobj)

@ItemRouter.get('/',status_code=status.HTTP_200_OK)
def getAll(itemService:ItemService = Depends()):
    """
    requests every item entity to the service
    :param itemService: Instance of the service being called
    :return: every eitem entity
    """
    return itemService.getAll()

@ItemRouter.patch('/{codeobj}',status_code=status.HTTP_202_ACCEPTED)
def updateOne(codeobj: int,item:ItemSchema,itemService:ItemService = Depends()):
    """
    requests an update of the item with new data,on the corresponding entity
    :param codeobj: ID of the item to update, retrieved from the http request param
    :param item: data to send to update the entity
    :param itemService: Instance of the service being called
    :return: updated entity
    """
    return itemService.update(codeobj,item)

@ItemRouter.delete('/{codeobj}',status_code=status.HTTP_200_OK)
def deleteOne(codeobj: int,itemService:ItemService = Depends()):
    """
    requests a deletion of the item with the corresponding id to the service
    :param codeobj: ID of the item to delete, retrieved from the http request param
    :param itemService: Instance of the service being called
    :return: null, http code 200
    """
    return itemService.delete(codeobj)