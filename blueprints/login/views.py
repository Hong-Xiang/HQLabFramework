from flask import render_template, flash, redirect, session, url_for, g
from flask_login import login_user, login_required, logout_user
from hqlf.models.user import User
from hqlf import app, db, lm, oid
from hqlf.blueprints.login import login_pages
from hqlf.blueprints.login.forms import LoginForm


# index view function suppressed for brevity

@lm.user_loader
def user_loader(id):
    return User.query.get(id)


def check_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return None
    if user.password == password:
        return user
    else:
        return None


@login_pages.route('/login', methods=['GET', 'POST'])
# @oid.loginhandler
def login():
    # if g.user is not None and g.user.is_authenticated():
    #     return redirect(url_for('home'))
    message = ''
    form = LoginForm()
    if form.validate_on_submit():
        user = check_user(form.username.data, form.password.data)
        if user is not None:
            login_user(user)
            return redirect(url_for('home'))
        # session['remember_me'] = form.remember_me.data
        # return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login/login.html',
                           title='HQLF-Sign in',
                           form=form,
                           message=message)

lm.login_view = 'login_pages.login'


@login_pages.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_pages.login'))
