# -*- coding: utf-8 -*-
import sqlite3

# 连接
conn = sqlite3.connect('mydb.db')
c = conn.cursor()

# 查询方式一
for row in c.execute('SELECT * FROM voting'):
    print(row)
print "*********************"

# # 查询方式二
# c.execute('SELECT * FROM voting')
# print(c.fetchall())

# 查询方式二_2
res = c.execute('SELECT * FROM voting')
print(res.fetchall())

print "*********************"
# 查询方式二_2
res = c.execute('SELECT DISTINCT ideanum,sum(value) as s FROM voting group by ideanum order by s desc ')
print(res.fetchall())
print "*********************"



print "***************3******"
# 查询方式二_2
res3 = c.execute('SELECT DISTINCT voterid from voting ')
print(res3.fetchall())
print "**********3***********"


print "*********************"
# 查询方式二_2
res2 = c.execute('SELECT ideanum,gift,count(gift) as s FROM voting group by gift ')
print(res2.fetchall())
print "*********************"

print "************4*********"
# 查询方式二_2
res32 = c.execute('SELECT * from  msg')
print(res32.fetchall())
print "**********4***********"
print "************5*********"
# 查询方式二_2
res323 = c.execute('select ideanum,count(*) as m from msg group by ideanum')
print(res323.fetchall())
print "**********5***********"

count = c.execute('select count(*) from voting')
rs = count.fetchone()
print rs[0]
# 关闭
conn.close()