import mysql.connector
cn=mysql.connector.connect(host='localhost',user='admin',password='admin123',database='sample')
cn.autocommit=True
cur=cn.cursor()
# cur.execute("create database sample")
# cur.execute("create table user(no int,name text,age int)")
# no=int(input('Enter No:'))
# name=input('Enter Name:')
# age=int(input('Enter Age:'))
# cur.execute("insert into user(no,name,age)values(%s,%s,%s)",(no,name,age))

# cur.execute("select * from user")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("update user set age=28 where no=1")
# no=int(input('Enter No:'))
# name=input('Enter Name:')
# age=int(input('Enter Age:'))
# cur.execute("update user set name=%s,age=%s where no=%s",(name,age,no))

# cur.execute('select * from user')
# data=cur.fetchall()

# print('{:<10}{:<20}{:<7}'.format('No','Name','Age'))
# print('-'*35)
# for i in data:
#     print('{:<10}{:<20}{:<7}'.format(i[0],i[1],i[2]))

# cur.execute("select * from user order by name")
# data=cur.fetchall()
# cur.execute("select * from user order by name desc")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("create table address(no int,place text,pin int)")
# cur.execute("insert into address(no,place,pin)values(2,'mnl',665543),(3,'otp',695367),(4,'thr',695367)")
# cur.execute("select user.no,user.name,user.age,address.place,address.pin from user inner join address on user.no=address.no")
# cur.execute("select user.no,user.name,user.age,address.place,address.pin from user join address on user.no=address.no")
# cur.execute("select user.no,user.name,user.age,address.place,address.pin from user left join address on user.no=address.no")
# cur.execute("select user.no,user.name,user.age,address.place,address.pin from user right join address on user.no=address.no")
# data=cur.fetchall()
# for i in data:
#      print(i)
