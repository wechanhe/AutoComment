#!/usr/bin/python 
# -*- coding: UTF-8 -*-
import requests

msg_url ="http://msg.csdn.net/"
login_url = "https://passport.csdn.net/"

r = requests.get(msg_url, auth=('drfish', 'password'))

# 登陆
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

session = requests.session()
session.headers.update(headers)
r = session.get(login_url)
page = BeautifulSoup(r.text, "lxml")
authentication = {
    "username": "drfish",
    "password": "password",
    "lt": page.select("[name=lt]")[0]["value"],
    "execution": page.select("[name=execution]")[0]["value"],
    "_eventId": "submit",
}
r = session.post(login_url, authentication)
r2 = session.get(msg_url)
print(r2.text)

# 提交评论
blog_url = "http://blog.csdn.net/u013291394/comment/submit?id=50444369"
comment = {
    "content": "水军评论测试",
}
r2 = session.post(blog_url, comment)
print(r2.text)