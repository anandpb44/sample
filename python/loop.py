# for i in range(6):
#     print(i)
# i=6
# while(i>0):
#     print("*"*i)
#     i-=1
# for i in range(5,0,-1):
#     print("*"*i)
num=int(input("Enter No.:"))
r_num=0
a=num
while num != 0:
    digit=num%10
    r_num=r_num*10+digit
    num //=10     
if r_num==a:
    print("Yes")
else:
    print("Not")