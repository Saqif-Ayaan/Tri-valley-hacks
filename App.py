from flask import Flask

def initApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from Link import start
    from Link import detector
    from Link import info

    app.register_blueprint(start, url_prefix = '/')
    app.register_blueprint(detector, url_prefix = '/')
    app.register_blueprint(info, url_prefix = '/')

    return app
    