# -*- coding:utf-8 -*-
"""
第 0008 题：一个HTML文件，找出里面的正文。
"""

import requests,re
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/'
data=requests.get(url)
r = re.findall(r'<body(.*?)</body>',data.text)
print(r[0])
print('---------------------------------------------------------------')

# urls = re.findall(r'<a.*href=\"(.*?)\".*</a>',data.text)
# print(urls)

soup = BeautifulSoup(data.text,'html.parser')
print(soup.body.text)
urls = soup.findAll('a')
for u in urls:
    try:
        print(u['href'])
    except KeyError:
        pass