import pymysql

db = pymysql.connect("localhost","debian-sys-maint","YlWWL8vwQxM1rjM0")
cursor = db.cursor()
cursor.execute("create database indexdb;")
cursor.execute("use indexdb;")
cursor.execute("create table t1(id int,name char(20));")
n = 1
name="lucy"
while n <= 2000000:
    cursor.execute("insert into t1 values('%s','%s')" % (n,name+str(n)))
    # n = int(n)
    n += 1

db.commit()
cursor.close()
db.close()