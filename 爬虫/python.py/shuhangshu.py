# -*- coding:utf-8 -*-
# -*- coding: utf-8 -*-
import os
import re
exp_re = re.compile(r'^#.*')
file='kli.py'
file_path = 'dangdangTop500.py'
if  os.path.splitext(file_path)[1] == '.py':
    print('1')
    with open(file_path,'rb') as f:
        all_lines = 0
        space_lines = 0
        exp_lines = 0
        for line in f.readlines():
            all_lines += 1
            if line.strip() == '':
                space_lines += 1
                continue
            exp = exp_re.findall(line.strip().decode('utf-8'))
            if exp:
                exp_lines += 1
    print("%s\t%s\t%s\t%s" % (file, all_lines, space_lines, exp_lines))
print('2')