l=[]
limit=int(input("enter limit:"))
for i in range(limit):
    name=input('Name:')
    age=input('Age:')
    l.append({'name':name,'age':age})
print(l)