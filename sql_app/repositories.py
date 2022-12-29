from sqlalchemy.orm import Session
from . import models, schemas
import auth
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")







class ItemRepo:
    
 async def create(db: Session, item: schemas.ItemCreate):
        db_item = models.Item(name=item.name,sort=item.sort,description=item.description,id=item.id,owner_id=item.owner_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
 def fetch_by_id(db: Session,_id):
     return db.query(models.Item).filter(models.Item.id == _id).first()
 
 def fetch_by_name(db: Session,name):
     return db.query(models.Item).filter(models.Item.name == name).first()

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
 def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


 def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
 
 def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


 def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


 def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


 def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item



