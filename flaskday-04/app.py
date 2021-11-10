from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/base')
def load_base():
    return render_template('base.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/macro')
def use_macro():
    return render_template('macro/macro1.html')


@app.route('/macro1')
def use_macro1():
    return render_template('macro/macro2.html')


if __name__ == '__main__':
    print(app.url_map)
    app.run()
