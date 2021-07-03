import sqlalchemy as _sql
import datetime as _dt
import sqlalchemy.orm as _orm
import database as _database 

class Store(_database.Base):
    __tablename__ = "stores"
    id = _sql.Column('id',_sql.Integer,primary_key=True,index=True)
    name = _sql.Column('name',_sql.String(255))
    code = _sql.Column('code',_sql.String(255))
    active = _sql.Column('active',_sql.Boolean,default=True)
    created_at = _sql.Column('created_at',_sql.DateTime,default=_dt.datetime.utcnow)
    updated_at = _sql.Column('updated_at',_sql.DateTime,default=_dt.datetime.utcnow)
    address = _sql.Column('address',_sql.String(255))
    gst_no = _sql.Column('gst_no',_sql.Integer)
    email = _sql.Column('email',_sql.String(255),unique=True)
    mobile_no = _sql.Column('mobile_no',_sql.Integer,unique=True)
    service_tax = _sql.Column('service_tax',_sql.Integer)
    commission_percentage = _sql.Column('commission_percentage',_sql.Integer)
    is_online_payment = _sql.Column('is_online_payment',_sql.Boolean,default=True)