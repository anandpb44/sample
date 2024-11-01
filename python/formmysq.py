import mysql.connector
con=mysql.connector.connect(host='localhost',user='admin',password='admin123',database='form')
con.autocommit=True
cr=con.cursor()
# cr.execute("create database form")
# cr.execute("create table details(id int,name text,age int)")
# cr.execute("alter table details add column gender text")
# cr.execute("insert into details(id,name,age,gender)values(%s,%s,%s,%s)",)