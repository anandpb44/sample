print("1.Celcius To Fahrenheit")
print("2.Fahrenheit To Celcius")
print("3.celcius To Kelvin")
print("4.Fahrenheit To kelvin")
print("5.Kelvin To F")
print("6.Kelvin To C")
choice=float(input("Enter Your choice:"))
if choice==1:
    a=float(input("Celcius data:"))
    F=(a*9/5)+32
    print("F=",F)
elif choice==2:
    a=float(input("fahrenheit data:"))
    c=(a-32)*5/9
    print("C=",c)
elif choice==3:
    a=float(input("C="))
    k=a+273.15
    print("k=",k)
elif choice==4:
    a=float(input("F="))
    k=(a-32)*5/9+273.15
    print("K=",k)
elif choice==5:
    a=float(input("K="))
    f=(a-273.15)*9/5+32
    print("F=",f)
elif choice==6:
    k=float(input("K="))
    c=k-273.15
    print("C=",c)
else:
    print("Wrong Choice!!!")