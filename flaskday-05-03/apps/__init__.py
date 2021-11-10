from flask import Flask

import settings
from apps.user.view import user_bp
from ext import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    app.register_blueprint(user_bp)
    db.init_app(app)

    return app

