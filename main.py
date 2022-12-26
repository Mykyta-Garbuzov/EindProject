import uvicorn
import sql_app.models as models
import sql_app.schemas as schemas

from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from sql_app import models
from db import get_db, engine
from sql_app.repositories import ItemRepo
from sqlalchemy.orm import Session
from typing import List,Optional
from fastapi.encoders import jsonable_encoder

from fastapi.middleware.cors import CORSMiddleware





app = FastAPI(title="FastAPI Application",
    description=" FastAPI Application with Swagger and Sqlite",
    version="1.0.0",)

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if not (credentials.username == "admin@mysite.com") or not (credentials.password == "mykyta"):
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username 


@app.get("/users/me" )
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)

#Meld over een fout 
@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


@app.get('/dogs', tags=["Item"],response_model=List[schemas.Item])
def get_all_items(name: Optional[str] = None,db: Session = Depends(get_db)):
    """
    Get all the Items stored in database
    """
    if name:
        dogs =[]
        db_item = ItemRepo.fetch_by_name(db,name)
        dogs.append(db_item)
        return dogs
    else:
        return ItemRepo.fetch_all(db)


@app.get('/dogs/{item_id}', tags=["Item"],response_model=schemas.Item)
def get_item(item_id: int,db: Session = Depends(get_db)):
    """
    Get the Item with the given ID provided by User stored in database
    """
    db_item = ItemRepo.fetch_by_id(db,item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    return db_item



# @app.get('/dogs/{item_sort}', tags=["Item"],response_model=List[schemas.Item])
# def get_sort(item_sort:Optional[str] = None,db: Session = Depends(get_db)):
#     """
#     Get the Sort
#     """
#     db_item = ItemRepo.fetch_by_sort(db,item_sort)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found with the given ID")
#     return ItemRepo.fetch_by_sort(db)  










@app.delete('/dogs/{item_id}', tags=["Item"])
async def delete_item(item_id: int,db: Session = Depends(get_db)):
    """
    Delete the Item with the given ID provided by User stored in database
    """
    db_item = ItemRepo.fetch_by_id(db,item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found with the given ID")
    await ItemRepo.delete(db,item_id)
    return "Item deleted successfully!"

@app.put('/dogs/{item_id}', tags=["Item"],response_model=schemas.Item)
async def update_item(item_id: int,item_request: schemas.Item, db: Session = Depends(get_db)):
    """
    Update an Item stored in the database
    """
    db_item = ItemRepo.fetch_by_id(db, item_id)
    if db_item:
        update_item_encoded = jsonable_encoder(item_request)
        db_item.name = update_item_encoded['name']
        db_item.price = update_item_encoded['sort']
        db_item.description = update_item_encoded['description']
        db_item.store_id = update_item_encoded['store_id']
        return await ItemRepo.update(db=db, item_data=db_item)
    else:
        raise HTTPException(status_code=400, detail="Item not found with the given ID")
    
#Meld 
@app.post('/dogs', tags=["Item"],response_model=schemas.Item,status_code=201)
async def create_item(item_request: schemas.ItemCreate, db: Session = Depends(get_db)):
    """
    Create an Item and store it in the database
    """
    
    db_item = ItemRepo.fetch_by_name(db, name=item_request.name)
    if db_item:
        raise HTTPException(status_code=400, detail="Item already exists!")

    return await ItemRepo.create(db=db, item=item_request)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True,log_level="info")