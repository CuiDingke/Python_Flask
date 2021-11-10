class Config:
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bing:bing@39.107.138.229:3306/mysql_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 去除警告


# 开发环境
class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


# 生产环境
class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
