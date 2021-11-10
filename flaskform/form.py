import re

from flask import session
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo


# StringField
# PasswordField
# IntegerField  整型
# DecimalField  小数点
# FloatField   BooleanField
# 各种验证： DataRequired  EqualTo   IPAddress   Length   NumberRange   URL   Email   Regexp
class UserForm(FlaskForm):
    # StringField文本字段,DataRequired确保转换类型后字段中有数据,Length长度
    name = StringField(label='用户名', validators=[DataRequired(), Length(min=6, max=12, message='用户名长度必须在6至12位')])
    password = PasswordField(label='密码', validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6至12位')])
    confirm_pwd = PasswordField(label='确认密码', validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6至12位'),
                                                          EqualTo('password', '两次密码不一致')])
    phone = StringField(label='手机号码', validators=[DataRequired(), Length(min=11, max=11, message='手机号码必须为11位')])
    icon = FileField(label='用户头像', validators=[FileRequired(), FileAllowed(['jpg', 'png'], message='Images only!')])
    # 验证码
    # recaptcha = RecaptchaField(label='验证码')
    recaptcha_1 = StringField(label='验证码1')

    # 自己写限制条件  用户名不能以数字开头
    def validate_name(self, data):
        # 都是表单类型  返回的是一个表单<input id="name" name="name" required type="text" value="sun111">
        # print(self.name.data)
        # # <class 'wtforms.fields.core.StringField'>
        # print('==========>', type(self.name))
        # print(data)
        # print('==========>', type(data))
        if self.name.data[0].isdigit():
            raise ValidationError('用户名不能以数字开头')

    def validate_phone(self, data):
        # print(self.password.data)
        # print(data.data)
        phone = data.data
        if not re.search(r'^1[3578]\d{9}$', phone):
            raise ValidationError('手机号码格式错误')

    def validate_recaptcha_1(self, data):
        input_code = data.data
        code = session.get('code_valid')
        if input_code.lower() != code.lower():
            raise ValidationError('验证码错误')