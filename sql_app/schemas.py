from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    sort : str
    description: Optional[str] = None
    id: int
    owner_id: int
    store_id: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class StoreBase(BaseModel):
    name: str

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True