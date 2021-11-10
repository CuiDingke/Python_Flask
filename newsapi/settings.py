import os.path


class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Blogflask:blog@39.107.138.229:3306/blogflask'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:bing@127.0.0.1:3306/newsdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # secret_key
    SECRET_KEY = 'Cuidingke'
    # 项目路径  当前文件的文件夹的绝对路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态文件加路径
    STATIC_DIR = os.path.join(BASE_DIR, 'static')

    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # 头像的上传目录
    UPLOAD_ICON_DIR = os.path.join(STATIC_DIR, 'upload/icon')
    # 相册的上传目录
    UPLOAD_PHOTO_DIR = os.path.join(STATIC_DIR, 'upload/photo')

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '39.107.138.229'
    CACHE_REDIS_PORT = 6379


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False


# 单独运行下
if __name__ == '__main__':
    # print(Path(Config.UPLOAD_ICON_DIR).as_posix())
    print(Config.UPLOAD_ICON_DIR)
    print(Config.BASE_DIR)
    print(os.path.abspath(__file__))
