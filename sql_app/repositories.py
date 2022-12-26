from sqlalchemy.orm import Session
from . import models, schemas

class ItemRepo:
    
 async def create(db: Session, item: schemas.ItemCreate):
        db_item = models.Item(name=item.name,sort=item.sort,description=item.description,id=item.id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
 def fetch_by_id(db: Session,_id):
     return db.query(models.Item).filter(models.Item.id == _id).first()
 
 def fetch_by_name(db: Session,name):
     return db.query(models.Item).filter(models.Item.name == name).first()

#  def fetch_by_sort(db: Session,sort,limit: int = 100):
#      return db.query(models.Item).offset(sort).limit(limit).all()
 
 def fetch_all(db: Session, skip: int = 0, limit: int = 100):
     return db.query(models.Item).offset(skip).limit(limit).all()
 
 async def delete(db: Session,item_id):
     db_item= db.query(models.Item).filter_by(id=item_id).first()
     db.delete(db_item)
     db.commit()
     
     
 async def update(db: Session,item_data):
    updated_item = db.merge(item_data)
    db.commit()
    return updated_item




