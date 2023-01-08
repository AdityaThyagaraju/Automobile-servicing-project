from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class Customer(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(20))
    username = db.Column(db.String(20))
    vehicles = db.relationship('Customerveh')
    notes = db.relationship('Note')

class Customerveh(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String(50))
    model = db.Column(db.String(50))
    chasis_no = db.Column(db.Integer,primary_key=True)
    selected_date = db.Column(db.DateTime)
    selected_slot = db.Column(db.Integer)
    cust_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    accept_by_staff = db.Column(db.Integer,default=0)
    requests = db.relationship('ReqSer')

class ReqSer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    veh_id = db.Column(db.Integer,db.ForeignKey('customerveh.id'))
    req = db.Column(db.String(50))

class CustFeedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cust_id = db.Column(db.Integer,db.ForeignKey('customer.id'))
    feedback = db.Column(db.String(10000))

class Staff(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(20))
    username = db.Column(db.String(20))


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('customer.id'))