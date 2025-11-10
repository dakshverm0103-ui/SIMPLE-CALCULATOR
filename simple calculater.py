a=int(input("enter the first number"))
b=int(input("enter the second number"))
choice=input("enter your choice +,-,*,/")
if choice=="+":
    print(a+b)
elif choice=="-":
    print(a-b)
elif choice=="*":
    print(a*b)
elif choice=="/":
    print(a/b)
else:
    print("invalid choice")
