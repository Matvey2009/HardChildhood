from flask import render_template, request, redirect
from app import app, db
from model.user import User


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

    
@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    if request.method == 'POST':
        print(123)
    data = {
        'title': "Регестрация",
        'user': 'o'
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
    data = {
        'title': "About",
        'users': User.query.all()
    }
    return render_template('users.html', data=data)

@app.route('/createusers',  methods = ['GET', 'POST'])
def createusers():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        user = User(name = name, description = description)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/users')
        except:
            return "Ошибка: 0xa0010011c"
    else:
        data = {
            'title': "Создать пользователя",
            'users': User.query.all()
        }
        return render_template('createusers.html', data=data)
 

@app.route('/user/<int:id>')
def user(id):
    user = User.query.get(id)
    return render_template('user.html', data=user)

@app.route('/user/<int:id>/delete')
def user_delete(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return redirect('/users')
    except:
        return "Не получилось"
    
@app.route('/user/<int:id>/update', methods=['GET', 'POST'])
def user_update(id):
    user = User.query.get(id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        user = User(name = name, description = description)
        try:
            #db.session.update(user)
            db.session.commit()
            return redirect('/users')
        except:
            return "Ошибка"
    else:
        return render_template('updtate.html', data=user)