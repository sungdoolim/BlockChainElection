from flask import Blueprint, render_template, make_response, flash, request, redirect, \
                  url_for, session
from flask_login import login_user, logout_user
from .forms import UserLoginForm
from models import Account

from models import db, db_add, db_flush
login_page = Blueprint('login_page', __name__, template_folder='templates', static_folder='static')

@login_page.route('status')
def status():
    return 'OK', 200
    
@login_page.route('/',  methods=['GET'])
def index():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = UserLoginForm()

    return render_template('views/login/index.html', form=form)

@login_page.route('/',  methods=['POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.

    form = UserLoginForm(request.form)
    username = form['username'].data
    password = form['password'].data
    print("username : ", username, "password : ", password)
    if form.validate():
        user = db.session.query(Account).filter(Account.username==username).first()#type: Account
        print(user)
        if user is not None and user.check_password(password):
            print(u"성공")
            # Login and validate the user.
            # user should be an instance of your `User` class
            login_user(user)

            #if not is_safe_url(next):
            #    return flask.abort(400)

            return '', 200
            #return redirect(next or url_for('index_page.status'))
    return '', 400
#    return render_template('views/login/login.html', form=form)

@login_page.route('/logout',  methods=['POST'])
def logout():
    logout_user()
    session.clear()

    return redirect(url_for('index_page.index'))