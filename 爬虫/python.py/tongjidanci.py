# -*- coding:utf-8 -*-
import re

with open('source0004.txt') as fin:
    str = fin.read()
    print(str)
reObj = re.compile('([\w]\w+[\w])')
words = reObj.findall(str)

wordDict = dict()

for word in words:
    if word.lower() in wordDict:
        wordDict[word.lower()] += 1
    else:
        wordDict[word] = 1

for key, value in wordDict.items():
    print('%s: %s' % (key, value))