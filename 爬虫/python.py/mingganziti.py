# -*- coding:utf-8 -*-
'''
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''
import re
import os
word_filter=set()

with open('filtered_words.txt') as f:
    for w in f.readlines():
        word_filter.add(w.strip())

while True:
    s=input()
    if s=='exit1':
        break
    for w in word_filter:
        if w in s:
            s=s.replace(w,'*'*len(w))
    print(s)