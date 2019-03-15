import pymysql

conn = pymysql.connect(host='23.234.53.46', port=3306, user='root', passwd='123456', db='test', charset="utf8")
cr = conn.cursor()

#查询
cr.execute("select * from userinfo")
results = cr.fetchall()

print(type(results))

for line in results:
    print(line)

#增删改
