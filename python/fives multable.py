n=int(input('Enter the Number:'))
f=open('multitable','w')
for i in range(1,11):
    for j in range(1,n+1):
        print(i,'*',j,'=',i*j)
        f.write(str(i)+'x'+str(j)+'='+str(i*j)+'\n')
        f.write('\n')
