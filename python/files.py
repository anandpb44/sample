# f=open('py','x')
# f.write('welcome to all')
# f.write('  to pyton')
# f=open('demo','w')
# f.write('welcome back')
# f.write(str(123))
# f.write(str([1,2,3,4,5]))
# f=open('demo','a')
# f.write(  'python')
# n=int(input('Enter limit:'))
# f=open('demo','w')
# for i in range(n):
#     name=input('Enter name:')
#     f.write(name+'\n')
# f=open('demo','r')
# a=f.read(11)
# print(a)
# print('-'*30)
# # f.seek(0)
# b=f.read()
# print(b)
# a=f.readline(2)
# print(a)
# b=f.readline()
# print(b)
# c=f.readline()
# print(c)
# a=f.readlines()
# print(a)
# f.seek(0)
# letter=0
# cap=0
# w=0
# l=''
# for i in range(len(a)):
#     b=f.readline().strip()
#     c=b.split(' ')
#     for j in c:
#         if j!=' ':
#             w+=1
#         if len(j)>len(l):
#             l=j
#     for j in b:
#         if j!='' :
#             letter+=1
#             if j.isupper():
#                 cap+=1
# print('letters=',letter)
# print('capital letters no:',cap)
# print('small letter no:',letter-cap)
# print('words no:',w)
# print(l)
import os
# if os.path.exists('demo'):
#     os.remove('demo')
# else:
#     print('not')
# os.mkdir('demo')
# os.rmdir('demo')