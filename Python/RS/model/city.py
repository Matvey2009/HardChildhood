from datetime import datetime
from app import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key = True) #Айди
    name=db.Column(db.String(255), nullable = False)#Имя

