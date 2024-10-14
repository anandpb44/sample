def admin():
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
                        id=100
                    else:
                        id=book[-1]['id']+1
                        print(id)
                    
                    name=input('enter name:')
                    stock=int(input('No of Stock:'))
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
                          print('{:<14}{:<12}{:<20}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))
                elif ch1==5:
                      print('{:<14}{:<12}{:<20}{:<10}'.format('id','Name','Email','phone'))
                      for i in user:
                          print('{:<14}{:<12}{:<20}{:<10}'.format(i['id'],i['name'],i['email'],i['phone']))
                elif ch1==6:
                    break
                else:
                    print('invalid choice!')