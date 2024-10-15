user=[]
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
                print('user login')
                f=2
                users=i
    if f==0:
        print('invalid user name or password!!!')
    return f,users