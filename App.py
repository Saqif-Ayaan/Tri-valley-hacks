from flask import Flask

def initApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from Link import start

    app.register_blueprint(start, url_prefix = '/')

    return app
    