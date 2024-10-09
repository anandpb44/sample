user=[]
book=[]
def reg():
    if len(user)==0:
        id=101
            
    else:
        id=user[-1]['id']+1
        print(id)
    name=input('enter name:')
    email=input('enter email:')
    phno=int(input('enter phone no:'))
    password=input('enter password:')
    user.append({'id':id,'name':name,'email':email,'phone':phno,'password':password,'book':[]})
def log():
    uname=input('enter user name:')
    password=input('enter password:')
    f=0
    users=''
    if uname=='admin' and password=='admin':
        print('admin login')
        f=1
    if uname.isdigit():
        uname=int(uname)
        for i in user:
            if i['id']==uname and i['password']==password:
                f=2
                users=i
    if f==0:
        print('invalid user name or password!!!')
    return f,users
def add_book():
    if len(book)==0:
        id=100
    else:
        id=book[-1]['id']+1
        print(id)

    name=input('enter name:')
    stock=int(input('No of Stock:'))
    price=int(input('enter price:'))
    book.append({'id':id,'name':name,'stock':stock,'price':price})
def update():
    id=int(input('enter id:'))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            i['name']=input('enter new name:')
            i['stock']=int(input('enter stock no:'))
            i['price']=int(input('price:'))
            if f1==0:
                print('book not available!')
def delete():
     id=int(input('entert id:'))
     f1=0
     for i in book:
        if i['id']==id:
            f1=1
            book.remove(i)
     if f1==0:
        print('invalid')
def view_book():
    print('{:<14}{:<12}{:<20}{:<10}'.format('id','Name','stock','price'))
    for i in book:
        print('{:<14}{:<12}{:<20}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))
def view_user():
    print('{:<14}{:<12}{:<20}{:<10}'.format('id','Name','Email','phone'))
    for i in user:
        print('{:<14}{:<12}{:<20}{:<10}'.format(i['id'],i['name'],i['email'],i['phone']))
def view_prof():
    print(users)

while True:
    print('''
          1.Register
          2.Login
          3.Exit''')
    ch=int(input('enter choice:'))
    if ch==1:
        reg()
    elif ch==2:
        f,users=log()
        if f==1:
            while True:
                print('''
                      1,add book
                      2.update
                      3.delete
                      4.view book
                      5.view user
                      6.exit''')
                ch1=int(input('enter choice:'))
                if ch1==1:
                    add_book()
                elif ch1==2:
                    update()
                elif ch1==3:
                    delete()
                elif ch1==4:
                    view_book()
                elif ch1==5:
                    view_user()
                elif ch1==6:
                    break
                else:
                    print('invalid choice !!!')
            
        elif f==2:
            print('user')
            while True:
                print('''
                          1.view profile
                          2.lend book
                          3.return book
                          4.books in hand
                          5.log out''')
                ch2=int(input('enter choice:'))
                if ch2==1:
                    view_prof(users) 
        else:
            print('invalid')