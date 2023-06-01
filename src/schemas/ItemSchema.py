from pydantic import BaseModel
from typing import Optional



class ItemSchema(BaseModel):
    libobj: Optional[str]
    tailleobj: Optional[str]
    puobj: Optional[float]
    poidsobj: Optional[float]
