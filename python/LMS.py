user=[]
book=[]
while True:
    print('''
          1.Register
          2.Login
          3.Exit''')
    ch=int(input('enter choice:'))
    if ch==1:
        if len(user)==0:
            id=1
            
        else:
            id=user[-1]['id']+1
            print(id)
        name=input('enter name:')
        email=input('enter email:')
        phno=int(input('enter phone no:'))
        password=input('enter password:')
        user.append({'id':id,'name':name,'email':email,'phnoeno':phno,'password':password})
    elif ch==2:
        uname=input('enter user name:')
        password=input('enter password:')
        f=0
        if uname=='admin' and password=='admin':
            print('admin login')
            f=1
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
                    if len(book)==0:
                        id=101
                    else:
                        id=book[-1]['id']+1
                        print(id)
                    
                    name=input('enter name:')
                    stock=int(input('enter no of it:'))
                    price=int(input('enter price:'))
                    book.append({'id':id,'name':name,'stock':stock,'price':price})
                elif ch1==2:
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
                elif ch1==3:
                    id=int(input('entert id:'))
                    f1=0
                    for i in book:
                        if i['id']==id:
                            f1=1
                            book.remove(i)
                    if f1==0:
                        print('invalid')
                elif ch1==4:
                      print('{:<14}{:<12}{:<20}{:<10}'.format('id','Name','stock','price'))
                      for i in book:
                          print('{:<14}{:<12}{:20}{:10}'.format(i['id'],i['name'],i['stock'],i['price']))
                elif ch1==5:
                      print('{:<14}{:<12}{:<20}{:<10}'.format('id','Name','Email','phno'))
                      for i in user:
                          print('{:<14}{:<12}{:20}{:10}'.format(i['id'],i['name'],i['email'],i['phno']))
                elif ch1==6:
                    break
                else:
                    print('invalid choice!')
        if uname.isdigit():
            uname=int(uname)
        for i in user:
            if i['id']==uname and i['password']==password:
                print('user login')
                f=2
            if f==0:
                print('invalid')
    elif ch==3:
        break
    else:
        print('invalid choice')            