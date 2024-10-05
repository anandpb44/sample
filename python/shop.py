user=[]
pro=[]
while True:
    print('''
          1.Register
          2.Log in
          3.Exit''')
    ch=int(input('Enter choice:'))
    if ch==1:
        if len(user)==0:
            id=101
        else:
            id=user[-1]['id']+1
            print(id)
        name=input('Enter Your Name:')
        email=input('Enter Your Email:')
        phone=int(input('Enter Phone No:'))
        password=input('Enter Your Password:')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'pro':[]})
    elif ch==2:
        uname=input('Enter user Name:')
        password=input('Enter Password:')
        f=0
        if uname=='admin' and password=='admin':
            print('Admin Login Page')
            f=1
            while True:
                print('''
                      1.Add Devices
                      2.Update Devices
                      3.View Devices
                      4.vVew Buyers
                      5.Exit''')
                ch1=int(input('Enter Choice:'))
                if ch1==1:
                    if len(pro)==0:
                        id=1003
                    else:
                        id=pro[-1]['id']+1
                        print(id)
                    model=input('Model Name:')
                    brand=input('Enter Brand Name:')
                    storage=input('Enter Storage:')
                    stock=int(input('Stock:'))
                    price=int(input('Enter price:'))
                    pro.append({'id':id,'model':model,'brand':brand,'storage':storage,'stock':stock,'price':price})
                elif ch1==2:
                    id=int(input('Enter id:'))
                    f1=0
                    for i in pro:
                        if i['id']==id:
                            f1=1
                            i['model']=input('Model Name:')
                            i['brand']=input('Enter Brand Name:')
                            i['storage']=input('Enter Storage:')
                            i['stock']=int(input('Stock:'))
                            i['price']=int(input('Enter price:'))
                    if f1==0:
                        print('product not available!')
                elif ch1==3:
                    print('{:<12}{:<20}{:<20}{:<10}{:<12}{:<20}'.format('ID','MODEL','BRAND NAME','STORAGE','STOCK','PRICE'))
                    for i in pro:
                        print('{:<12}{:<20}{:<20}{:<10}{:<12}{:<20}'.format(i['id'],i['model'],i['brand'],i['storage'],i['stock'],i['price']))
                elif ch1==4:
                    print('{:<10}{:<15}{:<20}{:<10}'.format('ID','NAME','EMAIL','PHONE'))
                    for i in user:
                         print('{:<10}{:<15}{:<20}{:<10}'.format(i['id'],i['name'],i['email'],i['phone']))
                elif ch1==5:
                    break
                else:
                    print('Invalid Choice!')
        if uname.isdigit():
            uname=int(uname)
        for i in user:
            if i['id']==uname and i['password']==password:
                print("Buyer Login")
                f=2
                while True:
                    print('''
                          1.View Devices
                          2.purchase Device
                          3.search Device
                          4.Exit''')
                    ch2=int(input('Enter Your choice:'))
                    if ch2==1:
                        print('{:<12}{:<20}{:<20}{:<10}{:<12}{:<20}'.format('ID','MODEL','BRAND NAME','STORAGE','STOCK','PRICE'))
                        for j in pro:
                            print('{:<12}{:<20}{:<20}{:<10}{:<12}{:<20}'.format(j['id'],j['model'],j['brand'],j['storage'],j['stock'],j['price']))
                    elif ch2==2:
                        model=input('Enter Name:')
                        f1=0
                        for j in pro:
                            if j['model']==model:
                                f1=1
                                if j['stock']>0:
                                    i['pro'].append(id)
                                    j['stock']-=1
                                else:
                                    print('Out of Stock !!!')
                        if f1==0:
                            print('Device Not available !!')
                    elif ch2==3:
                        model=input('Enter name:')
                        f2=0
                        print('{:<12}{:<20}{:<20}{:<10}{:<12}{:<20}'.format('ID','MODEL','BRAND NAME','STORAGE','STOCK','PRICE'))

                        for j in pro:
                            if j['model']==model:
                                f2=1
                                # for j in pro:
                                print('{:<12}{:<20}{:<20}{:<10}{:<12}{:<20}'.format(j['id'],j['model'],j['brand'],j['storage'],j['stock'],j['price']))
                            else:
                                print('Out Of Stock!!')
                        if f2==0:
                            print('Device Not available!!!')
                    elif ch2==4:
                        break
                    else:
                        print('invalid choice!!')
    elif ch==3:
        break
    else:
        print('Invalid Choice!!')