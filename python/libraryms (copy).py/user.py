from admin import *
from relo import *
def view_book():
    print('{:<14}{:<12}{:<10}{:<10}'.format('id','Name','stock','price'))
    for j in book:
        print('{:<14}{:<12}{:<10}{:<10}'.format(j['id'],j['name'],j['stock'],j['price']))
def lend_book(users):
    id=int(input('enter id:'))
    f1=0
    for j in book:
        if j['id']==id:
            f1=1
            if j['stock']>0:
                users['book'].append(id)
                j['stock']-=1
            else:
                print('out of stock!')
    if f1==0:
        print('Book not available!')
def re_book(users):
    id=int(input('enter id:'))
    f1=0
    for j in book:
        if j['id']==id and id in users['book']:
            f1=1
            j['stock']+=1
            users['book'].remove(id)
    if f1==0:
        print('book not available!')
def book_in(users):
    if len(users['book'])==0:
        print('No books!')
    else:
        print(users['book'])