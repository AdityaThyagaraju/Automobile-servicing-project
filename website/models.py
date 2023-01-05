from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class Customer(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(20))
    username = db.Column(db.String(20))
    notes = db.relationship('Note')

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