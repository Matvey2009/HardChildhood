from flask import render_template, request, redirect
from app import app, db
from model.user import User
from model.city import City

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
        number = request.form['number']
        description = request.form['description']
        city_id = request.form['city_id']
        user = User(name = name, number = number, description = description, city_id = city_id)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/user/' + str(user.id))
        except:
            return "Ошибка: 0xa0010011c"
    else:
        data = {
            'title': "Создать пользователя",
            'city_id': City.query.all()
        }
        return render_template('createusers.html', data=data)
 

@app.route('/user/<int:id>')
def user(id):
    user = User.query.get(id)
    user.city_id = City.query.get(user.city_id).name
    data = {
        'title': "Создать пользователя",
        'user': user
    }    
    return render_template('user.html', data=data)

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
        user.name = request.form['name']
        user.description = request.form['description']
        user.city_id = request.form['city_id']
        try:
            db.session.commit()
            return redirect('/user/' + str(id))
        except:
            return "Ошибка"
    else:
        data = {
            'title': "Редактирование пользователя",
            'user': user,
            'city': City.query.all()
        }
        return render_template('update.html', data=data)