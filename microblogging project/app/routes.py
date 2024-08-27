from flask.helpers import redirect
from flask.wrappers import Request
from app import app
from flask import render_template, url_for, flash, request

from app.forms import Edit_about_me, Login_form, Registration_form
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from app import db


@app.route("/tp")
def tp():
    return "Hii"


@app.route('/')
@app.route('/index')
@login_required
def index():
    title = 'microblog'
    data = [{
        "user": {
            "author": "vivek",
            "email": "vivek@gmail.com"
        },
        "post": "Good Morning"
    }, {
        "user": {
            "author": "Saurabh",
            "email": "saurabh@gmail.com"
        },
        "post": "Good Morning all !!!!"
    }, {
        "user": {
            "author": "Amit",
            "email": "amit@gmail.com"
        },
        "post": "Good Morning,have a nice day"
    }, {
        "user": {
            "author": "Appa",
            "email": "aappa@gmail.com"
        },
        "post": "Good Morning all"
    }]
    return render_template("index.html", data=data, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'login'
    if current_user.is_authenticated:
        return redirect('/index')
    form = Login_form()
    if form.validate_on_submit():
        flash(f'Login request for user { form.username.data }')
        myuser = User.query.filter(User.username == form.username.data).first()
        if myuser:
            if myuser.username == form.username.data and myuser.check_password(
                    form.password.data):
                flash('Logged in successfully.')
                login_user(myuser, remember=form.remember_me.data)
                return redirect(url_for('index'))
                # next_page=request.args.get('next')
                # if not next_page or url_parse(next_page).netloc != '':
                #     return redirect('/index')
                # return redirect(next_page)
            else:
                flash('Username or Password is invalid')
    return render_template('login.html', form=form, title=title)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration_form()
    title = 'register'
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, user_email=email)
        user.set_password_hash(password)
        db.session.add(user)
        db.session.commit()
        flash('You are registered successfully')
        return redirect(url_for('login'))

    return render_template('register.html', title=title, form=form)


@app.route('/mypage/<username>')
@login_required
def mypage(username):
    user = User.query.filter(User.username == username).first()
    posts = [{
        'author': user,
        "body": "First Post"
    }, {
        'author': user,
        "body": "Second Post"
    }]
    return render_template('mypage.html', user=user, posts=posts)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/edit_about_me/<username>', methods=['GET', 'POST'])
@login_required
def edit_about_me(username):
    form = Edit_about_me()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            edited_field = form.about_me.data
            current_user.about_me = edited_field
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for('mypage', username=current_user.username))

    return render_template('edit_about_me.html', title='edit_page', form=form)
