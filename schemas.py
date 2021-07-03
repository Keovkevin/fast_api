import pydantic as _pydantic
import datetime as _dt

class Store(_pydantic.BaseModel):
    id:int
    name:str
    code:str
    active:bool
    address:str
    gst_no:int
    email:str
    mobile_no:int
    service_tax:int
    commission_percentage:int 
    is_online_payment:bool

    class config:
        orm_mode=True

class StoreUpdate(_pydantic.BaseModel):
    name:str
    code:str
    address:str
    mobile_no:int
    email:str

    class config:
        orm_mode=True
