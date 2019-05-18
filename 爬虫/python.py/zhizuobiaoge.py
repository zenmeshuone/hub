# -*- coding:utf-8 -*-
import xlwt,json
from collections import OrderedDict
with open('student.txt','r') as f:
    data = json.load(f,object_pairs_hook=OrderedDict)
    workbook = xlwt.Workbook()
    sheet1 = workbook.add_sheet('student',cell_overwrite_ok=True)
    for index,(key,values) in enumerate(data.items()):
        print(index,key,values)
        sheet1.write(index,0,key)
        for i ,value in enumerate(values):
            print(i, value)
            sheet1.write(index,i+1,value)
    workbook.save('student.xls')