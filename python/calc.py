print("1.Additon")
print("2.Subtraction")
print("3.Divition")
print("4.Multiplication")
choice=int(input("Enter Your Choice:"))
if choice == 1:
    b=int(input("first no."))
    c=int(input("Second no."))
    sum=b+c
    print("Add:",sum)
elif choice == 2:
     b=int(input("first no."))
     c=int(input("Second no."))
     sub=b-c
     print("Sub:",sub)
elif choice == 3:
     b=int(input("first no."))
     c=int(input("Second no."))
     div=b/c
     print("Div:",div)
elif choice == 4:
     b=int(input("first no."))
     c=int(input("Second no."))
     mul=b*c
     print("Mul:",mul)
else:
    print("Wrong choice!!")
    