from datetime import datetime
from app import db
from model.city import City

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #Айди
    name=db.Column(db.String(255), nullable = False)#Имя
    number = db.Column(db.Integer, primary_key = False)
    date=db.Column(db.Date, default=datetime.utcnow) #Вр
    city_id=db.Column(db.Integer, db.ForeignKey(City.id), nullable = True)#Ключ города
