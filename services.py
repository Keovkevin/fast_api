import database as _database,models as _models,schemas as _schemas
import sqlalchemy.orm as _orm
import datetime as _dt

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db 
    finally:
        db.close()

def get_store_by_email(db:_orm.Session,email:str):
    return db.query(_models.Store).filter(_models.Store.email == email).first()

def create_store(db:_orm.Session,store:_schemas.Store):
    db_user = _models.Store(    
        name=store.name,
        code=store.code,
        active=store.active,
        address=store.address,
        gst_no=store.gst_no,
        email=store.email,
        mobile_no=store.mobile_no,
        service_tax=store.service_tax,
        commission_percentage=store.commission_percentage,
        is_online_payment=store.is_online_payment
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.__dict__

def get_stores(db:_orm.Session,skip:int,limit:int):
    stores = [i.__dict__ for i in db.query(_models.Store).offset(skip).limit(limit).all()]
    return stores

def get_active_stores(db:_orm.Session,skip:int,limit:int):
    active_stores = [i.__dict__ for i in db.query(_models.Store).filter(_models.Store.active==1).offset(skip).limit(limit).all()]
    return active_stores

def get_stores_by_id(db:_orm.Session,store_id:int):
    return db.query(_models.Store).filter(_models.Store.id==store_id).first().__dict__

def soft_delete_stores(db:_orm.Session,store_id:int):
    store = db.query(_models.Store).filter(_models.Store.id==store_id).first()
    store.active=0
    db.commit()
    db.refresh(store)
    return store.__dict__

def hard_delete_stores(db:_orm.Session,store_id:int):
    db.query(_models.Store).filter(_models.Store.id==store_id).delete()
    db.commit()

def update_stores(db:_orm.Session,store:_schemas.StoreUpdate,store_id:int):
    store_update = db.query(_models.Store).filter(_models.Store.id==store_id).first()
    print(store_update.name)
    print(store.name,store.mobile_no,store.email,store.code,store.address)
    store_update.name = store.name
    store_update.mobile_no=store.mobile_no
    store_update.email = store.email
    store_update.code = store.code
    store_update.address=store.address
    db.commit()
    db.refresh(store_update)
    return store_update.__dict__

