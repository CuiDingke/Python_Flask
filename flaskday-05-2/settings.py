class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bing:bing@39.107.138.229:3306/mysql_db'


class DenvelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
