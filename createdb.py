# -*- coding: utf-8 -*-
import sqlite3

# 连接
conn = sqlite3.connect('mydb.db')
c = conn.cursor()

# 创建表
# c.execute('''drop table if exists voting''')
# c.execute('''create table voting ( voterid INTEGER,  ideanum INTEGER, gift INTEGER,value INTEGER,comment string )''')
#
c.execute('''drop table if exists msg''')
c.execute('''create table msg (id integer primary key autoincrement,voterid INTEGER,  ideanum INTEGER, comment string ,ideaowner INTEGER )''')


# 数据
# 格式：月份,蒸发量,降水量
# purchases = [(1, 1,1,1,'test' ),
#              (1,1,2,2,'test2'),
#             ]
#
# # 插入数据
# c.executemany('INSERT INTO voting VALUES (?,?,?,?,?)', purchases)

# 提交！！！
conn.commit()

# 查询方式一
for row in c.execute('SELECT * FROM voting'):
    print(row)

# 查询方式二
c.execute('SELECT * FROM voting')
print(c.fetchall())

# 查询方式二_2
res = c.execute('SELECT * FROM voting')
print(res.fetchall())



# 查询方式二_2
res = c.execute('SELECT * FROM msg')
print(res.fetchall())

# 关闭
conn.close()