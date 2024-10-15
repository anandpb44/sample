from relo import *
book=[]

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
