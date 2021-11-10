class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bing:bing@39.107.138.229:3306/mysql_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
