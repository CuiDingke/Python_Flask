from flask import Blueprint, request, render_template, redirect

from apps.user.model import User

user_bp = Blueprint('user', __name__)

# 列表保存的是一个一个的用户对象
users = []


@user_bp.route('/user')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取post提价的数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')
            # 创建User对象
            user = User(username, password, phone)
            # 添加用户列表中
            users.append(user)
            return redirect('/user')
    return render_template('user/register.html')


@user_bp.route('/user/login', methods=['GET', 'POST'])
def login():
    return 'User login'


@user_bp.route('/user/logout', methods=['GET', 'POST'])
def logout():
    return 'User logout'


@user_bp.route('/user/del')
def del_user():
    # 获取传递来的username
    username = request.args.get('username')
    # 根据username找到用户列表中的user对象
    for user in users:
        if user.username == username:
            # 删除user
            users.remove(user)
            return redirect('/user')
    else:
        return '删除失败'


@user_bp.route('/user/update', methods=['POST', 'GET'])
def update_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        relaname = request.form.get('relaname')
        for user in users:
            if user.username == relaname:
                user.username = username
                user.password = password
                user.phone = phone
                return redirect('/user')
    else:
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                return render_template('user/update.html', user=user)
