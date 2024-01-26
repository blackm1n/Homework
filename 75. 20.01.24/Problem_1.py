from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_wtf.csrf import CSRFProtect
from models import db, User
from forms import LoginForm, RegisterForm, Button
from fernet import fernet

app = Flask('database')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = b'a1ecd45d0220617093552420e1237fc032c0d1731147d420dfdededa300f55a4'
csrf = CSRFProtect(app)
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.get('/')
def main_get():
    logged_in = True if request.cookies.get('email') else False
    context = {'logged_in': logged_in}
    form = Button()
    if logged_in:
        context['name'] = User.query.filter(User.email == request.cookies.get('email')).first().name
        context['surname'] = User.query.filter(User.email == request.cookies.get('email')).first().surname
    return render_template('main.html', **context, form=form)


@app.post('/')
def main_post():
    if request.cookies.get('email'):
        response = make_response(redirect(url_for('main_get')))
        response.delete_cookie('email')
    else:
        response = make_response(redirect(url_for('login_get')))
    return response


@app.get('/login/')
def login_get():
    if request.cookies.get('email'):
        return redirect(url_for('main_get'))
    form = LoginForm()
    return render_template('login.html', form=form)


@app.post('/login/')
def login_post():
    form = LoginForm()
    if form.validate():
        response = make_response(redirect(url_for('main_get')))
        response.set_cookie('email', form.email.data)
        return response
    return render_template('login.html', form=form)


@app.get('/register/')
def register_get():
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.post('/register/')
def register_post():
    form = RegisterForm()
    if form.validate():
        response = make_response(redirect(url_for('login_get')))
        add_user(form.name.data, form.surname.data, form.email.data, fernet.encrypt(form.password.data.encode()))
        return response


def add_user(name, surname, email, password):
    user = User(name=name, surname=surname, email=email, password=password)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    app.run()
