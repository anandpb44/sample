l=[]
while True:
    print('''
          1.Add Std
          2.View Std
          3.update std
          4.Delete std
          5.Exit''')
    ch=int(input("Choice:"))
    if ch==1:
        roll_no=int(input('Roll No:'))
        name=input('Name:')
        email=input('Email:')
        cur=input('Course:')
        l.append({'roll_no':roll_no,'name':name,'email':email,'course':cur})
    elif ch==2:
        print('{:<14}{:<12}{:<20}{:<10}'.format('Roll no','Name','Email','Course'))
        for i in l:
            print('{:<14}{:<12}{:20}{:10}'.format(i['roll_no'],i['name'],i['email'],i['course']))
    elif ch==3:
        roll_no=int(input('roll no:'))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                name=str(input('name:'))
                email=input('email:')
                i['name']=name
                i['email']=email
                f=1
        if f==0:
            print('id not available!')
    elif ch==4:
        roll_no=int(input('roll no:'))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                l.remove(i)
                f=1
        if f==0:
            print('invalid roll no!')
    elif ch==5:
        break
    else:
        print('invalid ch')
        