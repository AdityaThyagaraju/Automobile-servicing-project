from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    role = db.Column(db.String(10))
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(20))
    username = db.Column(db.String(20))
    vehicles = db.relationship('Customerveh')
    notes = db.relationship('Note')
    bills = db.relationship('Staffbill')

class Customerveh(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    chasis_no = db.Column(db.Integer,primary_key=True)
    selected_date = db.Column(db.DateTime)
    selected_slot = db.Column(db.Integer)
    cust_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    accept_by_staff = db.Column(db.Integer,default=0)
    requests = db.relationship('ReqSer')

class ReqSer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    veh_id = db.Column(db.Integer,db.ForeignKey('customerveh.id'))
    req = db.Column(db.String(50))

class CustFeedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cust_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    feedback = db.Column(db.String(10000))

class Staffbill(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cust_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(),default = func.now())
    items = db.relationship('Items')

class Items(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.Integer)
    bill_id = db.Column(db.Integer,db.ForeignKey('staffbill.id'))

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))