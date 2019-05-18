# -*- coding: utf-8 -*-
# 做为 Apple Store App 独立开发者，你要搞限时促销，
# 为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）

# -*- coding: utf-8 -*-
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import mysql.connector

import random
import string

import mysql.connector

forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        yield Re


def save_code():
    conn = mysql.connector.connect(user='root', password='', database='test')
    cursor = conn.cursor()
    codes = generate_code(200, 20)
    for code in codes:
        cursor.execute("INSERT INTO `code`(`code`) VALUES(%s)", params=[code])
    conn.commit()
    cursor.close()


if __name__ == '__main__':
    save_code()