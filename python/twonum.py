# num=[5,4,2,7]
# target=9
# for i in range(len(num)-1):
#     if num[i]+num[i+1]==target:
#         print([i,i+1])

num=[2,7,2,7]
target=9
for i in range(len(num)):
        for j  in range(len(num)):
            if num[i]+num[j]==target:
             print(i,j)
   
