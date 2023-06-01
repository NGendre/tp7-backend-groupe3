from sqlalchemy.orm import relationship

from src.models.BaseModel import Dictable,Base
from sqlalchemy import Column, Integer, String, Date, Numeric

from src.schemas.ItemSchema import ItemSchema


class ItemModel(Base,Dictable):
	__tablename__ = "t_objet"
	#this model is mapped to the table 't_objet'

	def CreateItemModelFromSchema(itemSchema: ItemSchema):
		newItem = ItemModel()
		newItem.libobj = itemSchema.libobj
		newItem.tailleobj = itemSchema.tailleobj
		newItem.puobj = itemSchema.puobj
		newItem.poidsobj = itemSchema.poidsobj
		return newItem

	codeobj = Column(Integer, primary_key=True)
	libobj = Column(String(50), default=None)
	tailleobj = Column(String(50), default=None)
	puobj = Column(Numeric, default=0.0000)
	poidsobj = Column(Numeric, default=0.0000)
	indispobj = Column(Integer, default=0)
	o_imp = Column(Integer, default=0)
	o_aff = Column(Integer, default=0)
	o_cartp = Column(Integer, default=0)
	points = Column(Integer, default=0)
	o_ordre_aff = Column(Integer, default=0)
	# condit = relationship("ObjetCond",back_populates='objets')