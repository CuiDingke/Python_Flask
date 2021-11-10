from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from apps.models.news_model import NewsType

news_bp = Blueprint('news', __name__)
api = Api(news_bp)

# 返回的对象格式  定义给客户端返回的格式
types_fields = {
    'id': fields.Integer,
    'date_time': fields.String(),
    'name': fields.String(attribute='type_name')
}

# 新闻类型Api
class NewsTypeApi(Resource):
    @marshal_with(types_fields)
    def get(self):
        types = NewsType.query.all()
        return types  # NewsType属于自定义的一个类型

# 传入

# 新闻的Api
class NewsListApi(Resource):
    # get=====>相当于获取  获取某个分类下的新闻
    def get(self):
        pass



api.add_resource(NewsTypeApi, '/types')


# 同源   协议+主机名+端口号   相同 才是同源
#后端
# 1.使用第三方扩展 flask-cors