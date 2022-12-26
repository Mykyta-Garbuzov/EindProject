from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    sort : str
    description: Optional[str] = None
    id: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
