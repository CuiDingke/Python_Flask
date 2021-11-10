from flask import Flask

from apps.user.view import user_db
from exts import db, api
from settings import DevelopmentConfig


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app=app)
    api.init_app(app=app)
    app.register_blueprint(user_db)
    return app