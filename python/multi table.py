n=int(input('Enter the Number:'))
f=open('mtable','w')
for i in range(11):
    print(n,'x',i,'=',n*i)
    f.write(str(i)+'x'+str(n)+'='+str(i*n)+'\n')