1.模板
网页====》模板引擎处理-----》模板
      render_template
{{ 变量 }}


{% if %} {% endif %}
for  black  macro with

{% extends '' %}
{% include '' %}
{% import '' as ..%}

过滤器
1. 通过方法添加
2. 装饰器


1.flask-script
pip install flask-script

使用里面的Manager进行命令得到管理和使用
manager = Manager(app=app)
manager.run()

命令终端:
python app.py runserver


# 自定义命令
@manager.command
def init():
    print('你好啊！！')
调用命令
python app.py init

《=============================================================》
pip install pymysql    建工路
pip install flask-sqlalchemy   实现ORM映射
pip install flask-migrate    发布命令工具

步骤:
1.配置数据库连接路径
class Config:
    # mysql+pymysql://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bing:bing@39.107.138.229:3306/mysql_db'


2.将映射和命令关联
    创建包exts
    __init__.py 中添加: db = SQLAlchemy()----------必须和app联系
    def creat_app():
        ....
        db.init_app(app)  # 关联上app
        return app
3.migrate
# 命令工具
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


4.创建模型
models.py
模型就是类  但是要继承db.model
class User(db.Model):    -----------映射的user表
加字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 逐渐自增
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

5.使用命令:
    a.强调。。。
       在app.py 中导入模型from apps.user.models import User  #  这个一定要导入 灰也没事
    b. 在终端使用命令
        python app.py db init  -------->产生一个文件夹migrations
        python app.py db magrate  --------》自动产生了一个版本文件
        python app.py db upgrate   -------->同步
        python app.py db downgrate  -------》降级


《=============================================================》

