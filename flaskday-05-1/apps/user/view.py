from flask import Blueprint, url_for

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def user_create():
    print(url_for('user.hah'))
    # print(url_for('user.register'))
    return '用户中心'


@user_bp.route('/register', endpoint='hah')
def register():
    return '用户注册'
