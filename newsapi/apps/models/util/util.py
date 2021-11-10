# 像网易云信发送请求，帮助后台发送短信息
import hashlib
import json
from time import time
import requests


def util_sendmsg(mobile):
    url = 'https://api.netease.im/sms/sendcode.action'
    data = {
        'mobile': mobile,  # 你的手机号码
    }
    AppSecret = '86b36e58e25e'
    AppKey = '07f216ca802c41457e1b229ab89b0678'
    # json类型
    Nonce = 'qweqdqwd12e01029i0dw0qwd'  # 这个字符串时随机的长度不大于128，随便设
    CurTime = str(int((time() * 1000)))  # 采用时间戳
    content = AppSecret + Nonce + CurTime
    CheckSum = hashlib.sha1(content.encode()).hexdigest()  # 对上述进行按要求哈希
    headers = {  # 设置请求头
        'AppKey': AppKey,
        'Nonce': Nonce,
        'CurTime': CurTime,
        'CheckSum': CheckSum
    }

    response = requests.post(url, data=data, headers=headers)  # 发送post请求
    str_result = response.text
    json_result = json.loads(str_result)

    return json_result

