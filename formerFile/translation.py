#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import random
import openpyxl
from openpyxl import Workbook
import requests

# 使用: 将要翻译的内容放到c:\_Work\source.xlsx的Sheet1的第1列

# set baidu develop parameter
apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
appid = '20191216000366578'
secretKey = 'i3pjXzZIbB4rXcZdbKcW'

# 翻译内容 源语言 翻译后的语言


def translateBaidu(content, fromLang='en', toLang='zh'):
    salt = str(random.randint(32768, 65536))
    sign = appid + content + salt + secretKey
    sign = hashlib.md5(sign.encode("utf-8")).hexdigest()

    try:
        paramas = {
            'appid': appid,
            'q': content,
            'from': fromLang,
            'to': toLang,
            'salt': salt,
            'sign': sign
        }
        response = requests.get(apiurl, paramas)
        jsonResponse = response.json()  # 获得返回的结果，结果为json格式
        dst = str(jsonResponse["trans_result"]
                  [0]["dst"])  # 取得翻译后的文本结果
        return dst
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print('translate begin...')
    content = input("输入文本：\n")
    print('ending...')
    print(translateBaidu(content))
