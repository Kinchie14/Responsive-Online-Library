from flask import Blueprint, render_template, redirect, url_for, flash
from .userform import LoginForm, SignupForm

user = Blueprint('user', __name__)

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', form = form)


@user.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    
    return render_template('signup.html', form = form)

