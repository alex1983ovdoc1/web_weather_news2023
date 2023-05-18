from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/users')


# user's form
# @app.route('/login')
@blueprint.route('/login')
def login():
    if current_user.is_authenticated:           # if user authenticated
        return redirect(url_for('news.index'))       # go start page
    title = 'Authorization'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


# processing login
@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('/ You going in site! / (user/views)')
            return redirect(url_for('news.index'))
    flash('/ Name or password not correct / (user/views)')
    # return redirect(url_for('user.login'))
    return redirect(url_for('user.login'))


# user logout
@blueprint.route('/logout')
def logout():
    logout_user()
    flash('/ You logout from site. / (user/views)')
    return redirect(url_for('news.index'))


# user registration
@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    form = RegistrationForm()
    title = 'Registration (user/views.py)'
    return render_template('user/registration.html', page_title=title, form=form)


# processing registration
@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You registered!!! (user/views.py)')
        return redirect(url_for('user.login'))
    flash('Please, enter correct data. (user/views.py)')
    return redirect(url_for('user.register'))

