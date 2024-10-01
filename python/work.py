a=int(input("Enter A Number:"))
d={0:'zero',1:'one',2:'Two',3:'Three',4:'Four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
n=0
value=''
while a>0:
    n=a%10
    a//=10
    demo=d[n]
    value=demo+value
    # print(n)
print(value)