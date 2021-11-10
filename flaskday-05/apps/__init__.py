from flask import Flask
import settings
from apps.user.view import user_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')  # app is a main object
    app.config.from_object(settings)
    # Blueprint
    app.register_blueprint(user_bp) # lock Blueprint
    print(app.url_map)
    return app
