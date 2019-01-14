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

'''
'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
            'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
            'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
            'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
            'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
            'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
            'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
            'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
'''
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