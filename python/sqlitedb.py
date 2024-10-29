import sqlite3
cn=sqlite3.connect("first.db")
try:
    cn.execute("create table user(no int,name text,age int)")
    cn.execute("create table address (no int,place text,pin int)")
except:
    print("Table Created")

# cn.execute("insert into user(no,name,age)values(1,'athul',22)")
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

# name=input('Enter name:')
# age=int(input('Enter Age:'))
# no=int(input('Enter No:'))
# cn.execute("update user set name=?,age=? where no=?",(name,age,no))
# cn.commit()

# no=int(input('Enter No:'))
# cn.execute("delete from user where no=?",(no,))
# cn.commit()

# data=cn.execute("select * from user where name like 'a%'")
# data=cn.execute("select * from user where name like '%u'")
# data=cn.execute("select * from user where name like '_r%'")
# for i in data:
#     print(i)

# data=cn.execute("select * from user order by name")
# data=cn.execute("select * from user order by name desc")
# for i in data:
#     print(i)

# cn.execute("insert into address(no,place,pin)values(2,'mnl',665543),(3,'otp',695367),(4,'thr',695367)")
# cn.commit()

# data=cn.execute("select user.no,user.name,user.age,address.place,address.pin from user inner join address on user.no=address.no")
# data=cn.execute("select user.no,user.name,user.age,address.place,address.pin from user join address on user.no=address.no")
# data=cn.execute("select user.no,user.name,user.age,address.place,address.pin from user left join address on user.no=address.no")
# data=cn.execute("select user.no,user.name,user.age,address.place,address.pin from user right join address on user.no=address.no")
# for i in data:
#     print(i)

# data=cn.execute("select name,age from user group by name")
# data=cn.execute("select name,min(age) from user group by name")
# data=cn.execute("select name,max(age) from user group by name")
# data=cn.execute("select name,count(age) from user group by name")
# data=cn.execute("select name,avg(age) from user group by name")
# data=cn.execute("select name,sum(age) from user group by name")
# for i in data:
    # print(i)