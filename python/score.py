a=input("Enter Name:")
b=float(input("Enter Score:"))

if b<=100 and b>=90:
    print("You passed\nExcellent\n Your grade is A\nscore",b)
elif b<=89 and b>=80 :
    print("You passed\nGood\n Your Grade Is B\nScore",b)
elif b<=79 and b>=70:
    print("You Passed\nSatisfactory\n Your Grade is C\nScore",b)
elif b<=69 and b>=60:
    print("You passed\nNeeds Improvement\nYour Grade is D\nScore",b)
elif b<=59 and b>=0:
    print("Failed\n Needs improvement\nGrade F\nScore",b)
else:
    print("not valid score!")
