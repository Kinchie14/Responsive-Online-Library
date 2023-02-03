## .website
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasdas'

    from website.users.user import user
    from website.core.home import home

    app.register_blueprint(user)
    app.register_blueprint(home)


    return app



