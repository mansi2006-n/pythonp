print("Welcome to calculator")
ch="yes"
while ch.lower()!="no":
    try:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))

        print("\nChoose an operation:")
        print("\n1:Addition")
        print("\n2:Subtraction")
        print("\n3:Multiplication")
        print("\n4:Division\n")

        operation=input("Enter your choice(1/2/3/4 ):")

        if operation=='1' or operation=='+':
            print(f"{a}+{b}={a+b}")
        elif operation=='2' or operation=='-':
            print(f"{a}-{b}={a-b}")
        elif operation=='3' or operation=='*':
            print(f"{a}*{b}={a*b}")
        elif operation=='4' or operation=='/':
            if b!=0:
              print(f"{a}/{b}={a/b}")
            else:
                print("not divisible by 0")
        else:
            print("invalid choice. please try again")
    except ValueError:
        print("invalid input. please enter numeric value")
    ch=input("\nDo you want to continue? (yes/no):")
    print()
print("program finished")