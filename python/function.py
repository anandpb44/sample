def number():
    a=int(input('Enter first no:'))
    b=int(input('Enter Second no:'))
    return a,b


def add():
    a,b=number()
    print(a+b)
def sub():
    a,b=number()
    print(a-b)
def mul():
    a,b=number()
    print(a*b)
def div():
    a,b=number()
    print(a/b)
while True:
    print('''
          1.Add
          2.Sub
          3.Mul
          4.Div''')
    ch=int(input('choice:'))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    else:
        print('wrong choice')