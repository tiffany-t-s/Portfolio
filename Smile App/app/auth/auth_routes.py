from app.main.models import User
from app.auth.auth_forms import RegistrationForm, LoginForm
from flask import render_template, flash, redirect, url_for

from app import db
from app.auth import auth_blueprint as bp_auth 
from flask_login import login_user, current_user, logout_user, login_required
import sqlalchemy as sqla

@bp_auth.route('/user/register', methods=['GET', 'POST'])
def register():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        user = User(username = rform.username.data,
                    email = rform.email.data)
        user.set_password(rform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, ' + user.username + ' you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('register.html', form = rform)

@bp_auth.route('/user/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        query = sqla.select(User).where(User.username == lform.username.data)
        user = db.session.scalars(query).first()
        if (user is None) or (user.check_password(lform.password.data) == False):
            return redirect(url_for('auth.login'))
        
        login_user(user, remember = lform.remember_me.data)
        flash('The user {} has successfully logged in!'.format(current_user.username))
        return redirect(url_for('main.index'))
    return render_template('login.html', form = lform)

@bp_auth.route('/user/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

