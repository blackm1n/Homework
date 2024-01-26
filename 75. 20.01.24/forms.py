from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, ValidationError
from models import User
from fernet import fernet
from types import NoneType


class Button(FlaskForm):
    pass

def InDatabase(form, field):
    if field.data not in [user.email for user in User.query.all()]:
        raise ValidationError('Данного пользователя не существует')

def EqualPassword(form, field):
    if isinstance(User.query.filter(User.email == form.email.data).first(), NoneType):
        raise ValidationError('Данного пользователя не существует')
    if field.data != fernet.decrypt(User.query.filter(User.email == form.email.data).first().password).decode():
        raise ValidationError('Неправильный пароль')

class LoginForm(FlaskForm):
    email = EmailField('Электронная Почта', validators=[DataRequired(), Email(), InDatabase])
    password = PasswordField('Пароль', validators=[DataRequired(), EqualPassword])

class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField('Электронная Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])