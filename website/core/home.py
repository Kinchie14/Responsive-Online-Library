from flask import Blueprint, render_template, redirect, url_for, flash

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home.html')