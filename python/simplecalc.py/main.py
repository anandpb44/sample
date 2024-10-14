import add
import sub
import div
import mul
from input import inp
while True:
    print('''
        1.add
        2.sub
        3.div
        4.mul''')
    ch=int(input('Enter choice:'))
    if ch==1:
        a,b=inp()
        add.add(a,b)
    elif ch==2:
        a,b=inp()
        sub.sub(a,b)
    elif ch==3:
        a,b=inp()
        div.div(a,b)
    elif ch==4:
        a,b=inp()
        mul.mul(a,b)
    