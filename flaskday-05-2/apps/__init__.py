from flask import Flask

import settings
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings.DenvelopmentConfig)
    app.register_blueprint(user_bp)
    db.init_app(app)
    return app
