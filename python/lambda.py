#lambda arg:exp
# def add(a,b):
#     print(a+b)
# add(10,12)
#     return a+b
# print(add(10,22))

# add=lambda a,b:print(a+b)
# add(5,5)

# add=lambda a,b:a+b
# print(add(11,11))


# a=lambda:print('Yooohooo')
# a()
# l=[1,2,3,4,5,6]
# a=[]
# for i in l:
# print(i**3)
#     a.append(i**3)
# print(a)
# a=map(lambda x:x**3,l)
# print(list(a))
# print(list(map(lambda x:x**3,l)))
# def sample(x):
#     return x**3
# print(list(map(sample,l)))
# for i in l:
#     if i%2==0:
#         print(i)
# a=filter(lambda x:x%2==0,l)
# print(list(a))

# def even(x):
#     return x%2==0
# print(list(filter(even,l)))

# l=['anand','deepu','hari','athul','dijin','hakkeem']
# #b=input("enter a letter/word:")
# # for i in l:
# #     if a in i:
# #         print(i)
# # a=input('enter letter:')
# #  b=filter(lambda i:a in i,l)
# #  print(list(b))
# # print(list(filter(lambda i:a in i,l)))
# a=[i for i in l if i  ]
# print(a)
l=['apple','orange','mango']
large=''
for i in l:
    if len(i)>len(large):
        large=i
print(i)
