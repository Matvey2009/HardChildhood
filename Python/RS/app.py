from flask import Flask, render_template


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
#registration