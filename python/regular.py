import re
# a='welcome to python welcome'
# print(re.sub('welcome','Welcome',a,1))
# print(re.findall('python',a))
# print(re.search('welcome',a))
# print(re.search('l',a))

# a='abc567Def'
# print(re.search('abcdef',a))
# print(re.search('[a-z]',a))
# print(re.search('[A-Z]',a))
# print(re.search('[A-z]',a))
# print(re.search('[abcDef]',a))
# print(re.search('a...',a))
# print(re.search('a.*',a))
# print(re.search('f.+',a))
# print(re.search('f.*',a))
# print(re.search('D.+',a))
# print(re.search('f.?',a))
# print(re.search('a.?',a))

# print(re.search('[a-z].*[A-Z]',a))
# print(re.search('[a-z][0-9][A-Z]',a))
# print(re.search('[a-z].*[0-9].*[A-Z]',a))
# print(re.search('[a-m].*[0-9].*[A-Z]',a))
# print(re.search('[a-m0-9A-Z]',a))


# a='7456789032'
# print(re.search('[6-9].{9}',a))
# if len(a)==10 and a.isdigit() and re.search('^[6-9].{9}',a):
#     print('valid')
# else:
#     print('invalid')

#EMAIL VALIDATION

# b=input('Enter Email:')
# # print(re.search('[a-z].{2}.*@gmail.com$',b))
# if re.search('[a-z].{2}.*@gmail.com$',b):
#     print("Valid Email")
# else:
#     print("Invalid Email")

#PASSWORD VALIDATION

p=input('Enter Password:')
print(re.search('[a-z0-9A-Z].{7}',p))