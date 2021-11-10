from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/projects/') # 路由定义‘/' 无论请求URL是否带有/ 都可以执行视图函数。如果请求的是有/ 浏览器做了一次重定向
def projects():
    return 'The project page'


@app.route('/about') # 如果请求about/  会显示Not Found
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run()
