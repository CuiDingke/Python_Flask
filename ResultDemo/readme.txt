什么是RESTful
（1）每一个URL代表着一种资源
（2）客户端和服务器之间，传递这种资源的某种表现层
（3）客户端通过四个HTTP动词（GET,POST,PUT,DELETE）,对服务器的资源进行操作，实现

Postman


pip install flask-restful

api = Api(app=app)

定义类视图
from flask_restful import Resource
Class xxxApi(Resource)
    def get(self):
        pass

api.add_resource(xxxApi,'/user')




函数视图
类视图
增加 修改  删除  查询  是通过请求方式完成的

路径产生：
api.add_resource(Resource的子类，'/user')
api.add_resource(Resource的子类，'/goods')

endpoint

http://127.0.0.1:5000/user?id=1&page=4
