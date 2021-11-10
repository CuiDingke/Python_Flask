from flask import Blueprint, request, render_template

from apps.user.models import User
from ext import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 与模型结合，完成数据库的添加
            # 1.创建对象
            user = User()
            # 2.给对象赋值
            user.username = username
            user.password = password
            user.phone = phone
            # 3.添加  将user对象添加到session中，（类似缓存）
            db.session.add(user)
            # 4.提交
            db.session.commit()
            return '用户注册成功'
        else:
            return '两次密码不一样'
    return render_template('user/register.html')
