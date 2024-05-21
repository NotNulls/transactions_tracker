from app import db
from datetime import datetime, time

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(64))
    date = db.Column(db.DateTime, default = datetime.now())
    price = db.Column(db.String(64))

    def __init__(self,description, date, price):
        self.description = description
        self.date = date
        self.price = price

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable=True)
