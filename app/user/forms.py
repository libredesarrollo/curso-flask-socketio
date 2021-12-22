from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('Nombre',validators=[ InputRequired() ])
    username = StringField('Usuario',validators=[ InputRequired() ])
    email = StringField('Email',validators=[ InputRequired() ])
    password = PasswordField('password',validators=[ InputRequired(), EqualTo('confirm') ])
    confirm = PasswordField('Confirmar password',validators=[ InputRequired() ])

class LoginForm(FlaskForm):
    username = StringField('Usuario',validators=[ InputRequired() ])
    password = PasswordField('password',validators=[ InputRequired() ])
    