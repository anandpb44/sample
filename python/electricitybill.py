u=int(input("Enter Unit:"))
pa=0
if u<100:
    pa=0
elif u<200:
    pa=(u-100)*5
    print(pa)
else:
    pa=(100*5)+(u-200)*10
    print(pa)