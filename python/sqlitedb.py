import sqlite3
cn=sqlite3.connect("first.db")
try:
    cn.execute("create table user(no int,name text,age int)")
except:
    print("Table Created")

# cn.execute("insert into user(no,name,age)values(1,'anand',20),(2,'akhil kumar',21),(3,'deepu',22)")
# cn.commit()
# no=int(input('Enter No:'))
# name=input('Enter Name:')
# age=int(input('Enter Age:'))
# cn.execute("insert into user(no,name,age)values(?,?,?)",(no,name,age))
# cn.commit()

# limit=int(input('Enter The Limit:'))
# for i in range(limit):
#     no=int(input('Enter No:'))
#     name=input('Enter Name:')
#     age=int(input('Enter Age:'))
#     cn.execute("insert into user(no,name,age)values(?,?,?)",(no,name,age))
#     cn.commit()
# data=cn.execute('select * from user')
# print(data)

# print('{:<10}{:<20}{:<7}'.format('No','Name','Age'))
# print('-'*35)
# for i in data:
#     print('{:<10}{:<20}{:<7}'.format(i[0],i[1],i[2]))

# no=int(input('Enter No:'))
# data=cn.execute("select * from user where no=?",(no,))
# print(data)

# print('{:<10}{:<20}{:<7}'.format('No','Name','Age'))
# print('-'*35)
# for i in data:
#     print('{:<10}{:<20}{:<7}'.format(i[0],i[1],i[2]))

# cn.execute("update user set name='nabeel',age=20 where no=8")
# cn.commit()

name=input('Enter name:')
age=int(input('Enter Age:'))
no=int(input('Enter No:'))
cn.execute("update user set name=?,age=? where no=?",(name,age,no))
cn.commit()