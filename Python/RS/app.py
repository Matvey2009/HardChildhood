from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True) #Айди
    name=db.Column(db.String(255), nullable = False)#Имя
    description=db.Column(db.Text,default="Не найдено")#
    date=db.Column(db.Date, default=datetime.utcnow) #Время

@app.route('/')
@app.route('/index')
def index():
    data = {
        'title': "Главная странница",
        'contener': "Введите любое число от 0 до 100"
    }
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    data = {
        'title': "About",
        'contener': "About contener"
    }
    return render_template('about.html', data=data)

@app.route('/registration')
def registration():
    data = {
        'title': "Регестрация"
    }
    return render_template('registration.html', data=data)

@app.route('/table')
def table():
    data = {
        'title': "Таблица"
    }
    return render_template('table.html', data=data)

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', data=users)

if __name__ == '__main__':
    app.run(debug=True)
#registration