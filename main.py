import fastapi as _fastapi
import services as _services, schemas as _schemas
import datetime as _dt
import sqlalchemy.orm as _orm
from typing import List

app = _fastapi.FastAPI()
_services.create_database()

@app.get("/all",response_model=List[_schemas.Store])
def read_data(skip:int=0,limit:int =10,db:_orm.Session=_fastapi.Depends(_services.get_db),):
    stores = _services.get_stores(db=db,skip=skip,limit=limit)
    return stores

@app.get("/active",response_model=List[_schemas.Store])
def read_data(skip:int=0,limit:int =10,db:_orm.Session=_fastapi.Depends(_services.get_db),):
    active_stores = _services.get_active_stores(db=db,skip=skip,limit=limit)
    return active_stores

@app.get("/{store_id}",response_model=_schemas.Store)
def read_data(store_id:int,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.get_stores_by_id(db=db,store_id=store_id)

@app.post("/",response_model=_schemas.Store)
def write_data(store: _schemas.Store,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = _services.get_store_by_email(db=db,email=store.email)
    if db_user:
        raise _fastapi.HTTPException(status_code=400,detail="Email already exists")
    return _services.create_store(db=db,store=store)

@app.put("/{store_id}",response_model=_schemas.Store)
def update_data(store_id:int,store:_schemas.StoreUpdate,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.update_stores(db=db,store=store,store_id=store_id)

@app.delete("/soft/{store_id}",response_model=_schemas.Store)
def delete_data(store_id:int,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.soft_delete_stores(db=db,store_id=store_id)

@app.delete("/hard/{store_id}",response_model=_schemas.Store)
def delete_data(store_id:int,db:_orm.Session=_fastapi.Depends(_services.get_db)):
    return _services.hard_delete_stores(db=db,store_id=store_id)