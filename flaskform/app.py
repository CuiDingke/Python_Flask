import os.path
import time
from io import BytesIO
from pathlib import Path

from flask import Flask, render_template, make_response, session
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_wtf import CsrfProtect
from werkzeug.utils import secure_filename

from form import UserForm
from util import generate_image

config = {'CACHE_TYPE': 'redis',
          'CACHE_REDIS_HOST': '39.107.138.229',
          'CACHE_REDIS_PORT': 6379
          }
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')

app = Flask(__name__)
cache = Cache(app, config=config)
CsrfProtect(app)
# 一定要设置SECRET_KEY  不然矫正不过
app.config['SECRET_KEY'] = 'FAHFHDSJAHFASHF'
app.config['ENV'] = 'Development'
# 公钥
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# 私钥
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_PARAMETERS = {'hl': 'zh', 'render': 'explicit'}
RECAPTCHA_DATA_ATTRS = {'theme': 'dark'}
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=2)
def hello_world():
    uform = UserForm()
    # 主要通过uform.validate_on_submit() 进行校验的
    if uform.validate_on_submit():
        name = uform.name.data
        password = uform.password.data
        phone = uform.phone.data
        icon = uform.icon.data
        filename = secure_filename(icon.filename)
        # print(name, password, phone)
        # print(type(icon))
        # os.path.abspath(__file__) 当前文件的绝对路径
        # os.path.dirname 取文件的名字
        # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # STATIC_DIR = os.path.join(BASE_DIR, 'static')
        # UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')
        icon.save(os.path.join(UPLOAD_DIR, filename))
        return '提交成功！！！'
    # time.sleep(10)
    return render_template('user.html', uform=uform)


@app.route('/user', methods=['GET', 'POST'])
# @cache.cached(timeout=20)
def hello_world1():
    return render_template('user.html', uform=uform)


@app.route('/image')
def get_image():
    im, code = generate_image(4)
    # 将IMAGE对象转成二进制
    buffer = BytesIO()
    im.save(buffer, "JPEG")
    # 读取为二进制流
    # buffer.read()
    buf_bytes = buffer.getvalue()
    # 保存验证码  保存在session中
    session['code_valid'] = code
    response = make_response(buf_bytes)
    response.headers['Content-Type'] = 'image/jpg'
    return response


# form与Bootstrap结合使用
@app.route('/use', methods=['GET', 'POST'])
def boot_form_user():
    uform = UserForm()
    return render_template('use.html', uform=uform)


if __name__ == '__main__':
    app.run(debug=True)
