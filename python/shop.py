user=[]
phone=[]
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
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password})
    elif ch==2:
        uname=input('Enter user Name:')
        password=input('Enter Password:')
        f=0
        if uname=='admin' and password=='admin':
            print('Admin Login Page')
            f=1
            while True:
                print('''
                      1.Add items
                      2.update item
                      3.View items
                      4.view Byers
                      5.exit''')
                ch1=int(input('Enter Choice:'))