from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.Integer,unique=True)
    role = db.Column(db.String(10))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(20))
    username = db.Column(db.String(20),unique=True)
    vehicles = db.relationship('Customerveh')
    feedback = db.relationship('Feedback')
    bills = db.relationship('Staffbill')

class Customerveh(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    chasis_no = db.Column(db.Integer,unique=True)
    cust_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    requests = db.relationship('ReqSer')
 

class Feedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))    

class ReqSer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    veh_id = db.Column(db.Integer,db.ForeignKey('customerveh.id'))
    selected_date = db.Column(db.DateTime)
    accept_by_staff = db.Column(db.Integer,default=0)
    req = db.Column(db.String(50))

class Staffbill(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cust_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    veh_id = db.Column(db.Integer,db.ForeignKey('customerveh.id'))
    order_id = db.Column(db.Integer,unique=True)
    date = db.Column(db.DateTime(),default = func.now())
    items = db.relationship('Items')
    payed = db.Column(db.Integer,default=0)

class Items(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    bill_id = db.Column(db.Integer,db.ForeignKey('staffbill.id'))
