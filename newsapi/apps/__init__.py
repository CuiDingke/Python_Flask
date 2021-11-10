from flask import Flask

from apps.apis.news_api import news_bp
from apps.apis.user_api import user_bp
from exts import db, cors, cache
from settings import DevelopmentConfig

config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_POST': 6379
}


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    db.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(news_bp)
    app.register_blueprint(user_bp)
    cors.init_app(app=app, supports_credentials=True)
    cache.init_app(app=app,config=config)
    print(app.url_map)
    return app
