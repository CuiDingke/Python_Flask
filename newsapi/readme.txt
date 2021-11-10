1.使用第三方扩展
flask-cors

from flask-cors import CORS
cors = CORS()

cors.init_app(app=app, supports_credentials=True)