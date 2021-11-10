from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from apps.user.model import *
from flask_script import Manager

from apps import create_app
from exts import db

app = create_app()
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
