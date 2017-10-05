# -*- coding: utf-8 -*-
import sqlite3

# 连接
conn = sqlite3.connect('mydb.db')
c = conn.cursor()

# 查询方式一
for row in c.execute('SELECT * FROM voting'):
    print(row)
#
# # 查询方式二
# c.execute('SELECT * FROM voting')
# print(c.fetchall())

# 查询方式二_2
res = c.execute('SELECT * FROM voting')
print(res.fetchall())

count = c.execute('select count(*) from voting')
rs = count.fetchone()
print rs[0]
# 关闭
conn.close()