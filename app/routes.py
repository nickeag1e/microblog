from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nickolay'}
    posts = [
        {
            'author': {'username': 'Dmitriy Ivanovich'},
            'body': 'Люблю Информатику'
        },
        {
            'author': {'username': 'Sophia Sergeevna'},
            'body': 'УЧИТЕСЬ БЛИН!'
        },
        {
            'author': {'username': 'Nickolay Igorevich'},
            'body': 'Flask is important thing'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"{form.username.data} sign in successfully")
        return redirect('/index')
    return render_template('login.html', title='LogIn', form=form)