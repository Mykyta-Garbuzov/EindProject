from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base
    
class Item(Base):
    __tablename__ = "dogs"
    
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True,index=True)
    sort = Column(String(80), nullable=False, index=True)
    description = Column(String(200))
    def __repr__(self):
        return 'ItemModel(name=%s, sort=%s,id=%s)' % (self.name, self.sort)
    
