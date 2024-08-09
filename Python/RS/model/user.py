from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #Айди
    name=db.Column(db.String(255), nullable = False)#Имя
    description=db.Column(db.Text,default="Не найдено")#
    date=db.Column(db.Date, default=datetime.utcnow) #Время

