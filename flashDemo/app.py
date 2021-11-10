import logging

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = 'hsdjjfaks'


#自己配置logging
# logger = logging.getLogger('flask.app')
# 如果只想有一套日志系统的话  name就直接是app
logger = logging.getLogger('app')
logger.setLevel(logging.INFO)  # Log等级总开关
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler("log1.txt")
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)


@app.route('/')
def index():
    logger.warning('首页的警告！！！')
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # 验证用户是否是admin
        if username == 'admin':
            flash('恭喜验证成功了！！！')
            flash('我是第二个flash！！')
            # flash('恭喜验证成功了！！！', 'Info')
            # flash('我是第二个flash！！', 'error')
            # return render_template('index.html')
            return redirect(url_for('index'))
        else:
            # app.logger.debug('这是一个debug测试')
            # app.logger.error('这是一个error测试')
            app.logger.warning('这是一个warning测试')
    return render_template('login.html', msg='')


if __name__ == '__main__':
    app.run(debug=True)
