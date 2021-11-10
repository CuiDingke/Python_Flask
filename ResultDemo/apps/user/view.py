import os.path

from flask import Blueprint, url_for
from flask_restful import Resource, marshal_with, fields, reqparse, inputs, marshal
from werkzeug.datastructures import FileStorage

from apps.user.model import User, Friend
from exts import api, db
from settings import Config

user_db = Blueprint('user', __name__, url_prefix='/api')


# 自定义返回的值  要继承Raw  然后return进行重写
class IsDelete(fields.Raw):  # 继承Raw
    def format(self, value):  # 定义个方法
        print('------------->', value)
        return '删除' if value else '未删除'  # 想要返回什么结果


# 返回的对象格式  定义给客户端返回的格式
resource_fields_1 = {
    'id': fields.Integer,
    'private_name': fields.String(attribute='username', default='匿名'),  # 指定与数据库username匹配
    # scheme 默认为 http
    'url': fields.Url('single_user', absolute=True, scheme='https')  # 商品，用户列表  通过点击要获取详情信息
}

# 返回的对象格式  定义给客户端返回的格式
resource_fields = {
    'id': fields.Integer,
    'private_name': fields.String(attribute='username', default='匿名'),  # 指定与数据库username匹配
    'password': fields.String,  # 默认与数据库的password匹配
    'udatetime': fields.DateTime,
    'isdelete': fields.String(attribute='isdelete'),
    # 使用自定义的返回值
    'isdelete1': IsDelete(attribute='isdelete'),
    'phone': fields.String
}

# 参数解析对象的限制 ===== 后端自行检查
# request.form.get  request.form.get request.cookies.get
# 文件  type=werkzeug.datastructures.FileStorage
# bundle_errors=True 把所有的错都过一遍
# bundle_errors= False 遇到错误停止  默认为False
parser = reqparse.RequestParser(bundle_errors=True)  # 解析对象
parser.add_argument('username', type=str, required=True, help='必须输入用户名',
                    location=['form'])  # location=['form']限制必须为post请求 表单的那种
parser.add_argument('password', type=inputs.regex(r'^\d{6,12}$'), required=True, help='必须输入6~12位数字密码',
                    location=['form'])
parser.add_argument('phone', type=inputs.regex(r'1[358]\d{9}$'), location=['form'])
parser.add_argument('hobby', action='append')  # 以列表的形式进行添加
parser.add_argument('icon', type=FileStorage, location=['files'])  # 以列表的形式进行添加


# 定义类视图
class UserResource(Resource):
    # get 请求的处理
    @marshal_with(resource_fields_1)
    def get(self):
        users = User.query.all()
        # 测试错误
        # userList = []
        # for user in users:
        #     userList.append(user.__dict__)
        # return {'num': len(users), 'userList': users[1]}
        return users

    @marshal_with(resource_fields)
    def post(self):
        # 解析传过来的所有的值 前端传过来值时，先把声明的格式进行校验在获取
        args = parser.parse_args()  # 先依据解析格式进行解析校验
        username = args.get('username')
        password = args.get('password')
        phone = args.get('phone')
        # 创建User对象
        user = User()
        user.username = username
        user.password = password
        icon = args.get('icon')
        if icon:
            upload_path = os.path.join(Config.UPLOAD_ICON_DIR, icon.filename)
            icon.save(upload_path)
            # 保存路径
            user.icon = os.path.join('upload/icon', icon.filename)
        if phone:
            user.phone = phone
        db.session.add(user)
        db.session.commit()
        return user

    def put(self):
        return {'msg': '===============>put'}

    def delete(self):
        return {'msg': '===============>delete'}


# 带有参数的类视图
class UserSimpleResource(Resource):
    @marshal_with(resource_fields)  # 将返回的对象user进行序列化
    def get(self, id):
        user = User.query.get(id)
        return user

    def put(self, uid):
        print('endpoint的使用', url_for('all_user'))
        return {'msg': 'ok'}

    def delete(self, uid):
        pass


user_friend_fields = {
    'username': fields.String,
    'nums': fields.Integer,
    # 将列表中的对象转一下  用于下面的序列化
    'friends': fields.List(fields.Nested(resource_fields))
}


class UserFriendResource(Resource):
    @marshal_with(user_friend_fields)
    def get(self, id):
        friends = Friend.query.filter(Friend.uid == id).all()
        user = User.query.get(id)
        friend_list = []
        for friend in friends:
            u = User.query.get(friend.fid)
            friend_list.append(u)
        # 第一种方法不用@marshal_with(user_friend_fields)
        # data = {
        #     'username': user.username,
        #     'nums': len(friends),
        #     # 列表中有字典 形成了套叠  怎样处理呢  用marshal处理  将friend_list自动转化为resource_fields结构 进行序列化
        #     'friends': marshal(friend_list, resource_fields)
        # }

        # 第二种方法  @marshal_with(user_friend_fields)
        data = {
            'username': user.username,
            'nums': len(friends),
            # 列表中有字典 形成了套叠  怎样处理呢  用marshal处理  将friend_list自动转化为resource_fields结构 进行序列化
            'friends': friend_list
        }
        return data


# 加访问路径
api.add_resource(UserResource, '/user', endpoint='all_user')  # 用all_user代替UserResource
api.add_resource(UserSimpleResource, '/user/<int:id>', endpoint='single_user')
api.add_resource(UserFriendResource, '/friend/<int:id>', endpoint='user_friend')
