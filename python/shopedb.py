import sqlite3
shope=sqlite3.connect("shope.db")
try:
    shope.execute("create table admin(ID int,DeviceName text,Stock int,Price int,Model text)")
except:
    print("Table Created")

while True:
    print('''
        1.Insert Devices
        2.View Devices
        3.Update Devices
        4.Delete Device
        5.Exit''')
    ch=int(input('Enter Choice:'))
    if ch==1:
        id=int(input('Enter ID:'))
        name=input('Enter DeviceName:')
        stock=int(input('Enter No Of Stock:'))
        price=int(input('Enter Price:'))
        model=input('Enter ModelName:')
        shope.execute("insert into admin(ID,DeviceName,Stock,Price,Model)values(?,?,?,?,?)",(id,name,stock,price,model))
        shope.commit()
    elif ch==2:
        list=shope.execute("select * from admin")
        print('{:<8}{:<20}{:<10}{:<10}{:<20}'.format('ID','DeviceName','Stock','Price','Model'))
        for i in list:
            print('{:<8}{:<20}{:<10}{:<10}{:<20}'.format(i[0],i[1],i[2],i[3],i[4]))
    elif ch==3:
        name=input("Enter Device Name:")
        stock=int(input('Enter No Of Stock:'))
        price=int(input('Enter Price:'))
        model=input('Enter ModelName:')
        id=int(input('Enter ID:'))
        shope.execute("update admin set DeviceName=?,Stock=?,Price=?,Model=? where ID=?",(name,stock,price,model,id))
        shope.commit()
    elif ch==4:
        id=int(input('Enter id:'))
        shope.execute("delete from admin where ID=?",(id,))
    elif ch==5:
        break
    else:
        print("Invalid choice!!!")
