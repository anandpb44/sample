import add,sub,div,mul
from input import inpu
while True:
    print('''
        1.Add
        2.Sub
        3.div
        4.Mul
        5.Exit''')
    ch=int(input('Enter Choice:'))
    if ch==1:
        a,b=inpu()
        add.add(a,b)
    elif ch==2:
        a,b=inpu()
        sub.sub(a,b)
    elif ch==3:
        a,b=inpu()
        div.div(a,b)
    elif ch==4:
        a,b=inpu()
        mul.mul(a,b)
    elif ch==5:
        break
    else:
        print('invalid choice')
