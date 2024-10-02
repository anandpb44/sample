while True:
    print('''
          1.Add
          2.sub
          3.Div
          4.Mul
          5.Exit''')
    choice=float(input("Enter Your Choice:"))
    if choice == 1:
        b=int(input("first no."))
        c=int(input("Second no."))
        print(b+c)
    elif choice == 2:
         b=int(input("first no."))
         c=int(input("Second no."))
         print(b-c)
    elif choice == 3:
         b=int(input("first no."))
         c=int(input("Second no."))
         print(b/c)
    elif choice == 4:
        b=int(input("first no."))
        c=int(input("Second no."))
        print(b*c)
    elif choice==5:
        break
    else:
        print("Wrong choice!!")
        