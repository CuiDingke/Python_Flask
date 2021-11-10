class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xue:xue@39.107.138.229:3306/flaskblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
