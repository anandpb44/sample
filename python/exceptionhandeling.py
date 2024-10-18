# try:
#     print(10+'abc')
#     # print('no error')
# except:
#     print('an error')
# else:
#     print('no error')
# finally:


#     print('''
#     hallo
#     hi
#     hallo''')
# user=[]
# while True:
#     print('''
#           1.Register
#           2.Log in
#           3.Exit''')
#     while True:
#         try:
#             ch=int(input('Enter choice:'))
#             break
#         except:
#             pass
#     if ch==1:
#         if len(user)==0:
#             id=101
#         else:
#             id=user[-1]['id']+1
#             print(id)
#     name=input('Enter Your Name:')
#     email=input('Enter Your Email:')
#     phone=int(input('Enter Phone No:'))
#     password=input('Enter Your Password:')
#     user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'pro':[]})
l=[1,2,5.3,'abc',4.7,5,6]
sum=0
# for i in l:
#     if type(i)==int or type(i)==float:
#         sum+=i
# print(sum)
for i in l:
    try:
        sum+=i
    except:
        pass
print(sum)