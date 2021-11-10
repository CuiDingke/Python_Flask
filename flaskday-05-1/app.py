from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.user.models import User, UserInfo  #  这个一定要导入 灰也没事
from apps import creat_app
from exts import db

app = creat_app()
manager = Manager(app=app)  # 给app套了一层壳

# 命令工具
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


# 自定义命令
@manager.command
def init():
    print('你好啊！！')


if __name__ == '__main__':
    print(app.url_map)
    manager.run()
