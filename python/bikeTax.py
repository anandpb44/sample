p=int(input('Enter Bike Price:'))
t=0
if p>100000:
    t=p*15/100
    print('Price',p)
    print('Tax',t)
elif p>50000 and p<=100000:
    t=p*10/100
    print('Price',p)
    print('Tax',t)
elif p<=50000:
    t=p*5/100
    print('Price',p)
    print('Tax',t)
