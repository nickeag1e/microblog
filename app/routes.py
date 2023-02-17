from app import app
from flask import render_template


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
    return render_template('index.html',title='Home', user=user, posts=posts)
