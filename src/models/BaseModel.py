from sqlalchemy.orm import declarative_base

from src.config.Database import engine

Base = declarative_base()

def init():
    Base.metadata.create_all(bind=engine)

class Dictable:
    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])

    def to_dict_none_safe(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_") and self.__dict__.get(k) is not None])