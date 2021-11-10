from flask import Flask, request
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    print(request.headers)  # request对象 对象访问属性 也可以调用方法  headers path base_url url

    print(request.base_url)
    return 'Welcome BingL'


if __name__ == '__main__':
    app.run()
