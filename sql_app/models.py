from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship

from db import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    dogs = relationship("Item",primaryjoin="User.id == Item.owner_id",cascade="all, delete-orphan")

class Item(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True,index=True)
    sort = Column(String(80), nullable=False, index=True)
    description = Column(String(200))
    owner_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    store_id = Column(Integer,ForeignKey('stores.id'),nullable=False)


    def __repr__(self):
        return 'ItemModel(name=%s, sort=%s,id=%s,hashed_code=%s,store_id=%s)' % (self.store_id,self.name, self.sort,self.hashed_code)
    
class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True)
    dogs = relationship("Item",primaryjoin="Store.id == Item.store_id",cascade="all, delete-orphan")

    def __repr__(self):
        return 'Store(name=%s)' % self.name