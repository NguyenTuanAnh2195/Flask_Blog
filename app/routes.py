from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Tuan Anh'
    }

    posts = [
        {
            'author': {'username': 'Tuan Anh'},
            'body': 'Nghi covid o nha lam remote viet linh tinh'
        },
        {
            'author': {'username': 'cooler Tuan Anh'},
            'body': 'Khong duoc di an chan vl'
        }
    ]

    title = "Horror Story"

    render_response = {
        'user': user,
        'title': title,
        'posts': posts
    }

    return render_template('index.html', render_response=render_response)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'User {form.username.data} has logged in!')
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign In', form=form)
