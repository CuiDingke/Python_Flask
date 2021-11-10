from flask import Flask
import settings
from apps.user.view import user_bp
from exts import db


def creat_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../statics')
    app.config.from_object(settings.DevelopmentConfig)
    app.register_blueprint(user_bp)
    db.init_app(app)  # 关联上app
    return app
