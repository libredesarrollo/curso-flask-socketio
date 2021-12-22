from flask import Blueprint, render_template, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required

from app.user.models import User
from app.user.forms import RegisterForm, LoginForm
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

userBp = Blueprint('user',__name__)

@userBp.route('/register', methods=('GET','POST'))
def register():

    print(current_user)

    form = RegisterForm(meta={ 'csrf':False })

    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            print("Usuario duplicado")
        else:
            user = User()
            user.name = form.name.data
            user.username = form.username.data
            user.password = generate_password_hash(form.password.data)
            user.email = form.email.data

            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True)

            return redirect(url_for('user.register'))

    if form.errors:
        print(form.errors)

    return render_template('user/register.html',form=form)

@userBp.route('/login', methods=('GET','POST'))
def login():

    print(current_user)

    form = LoginForm(meta={ 'csrf':False })

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)

            return redirect(url_for('room.index'))

    if form.errors:
        print(form.errors)

    return render_template('user/login.html',form=form)

@userBp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))



