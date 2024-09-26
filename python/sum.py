# c=[1,3,6,3,9,11,]
# sum=sum(c)
# print(sum)
# sum=0
# for i in c:
#     sum=sum+i
#     print(i)
l=[1,2,4,8,10,56,22,"adc","dcb"]
sum=0
for i in l:
    if type(i)==int or type(i)==float:
        sum+=i
        print(sum)
 