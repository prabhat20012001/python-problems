num1=float(input("enter first num"))
num2=float(input("enter second number"))
op=input("enter operand")


if(op=="+"):
    print(f"addition of two number: {num1+num2}")
elif(op=="-"):
    print(f"subtraction of two number:{num1-num2}")
elif(op=="*"):
    print(f"mul of two number:{num1*num2}")
elif(op=="/"):
    print(f"div of two number:{num1/num2}")
elif(op=="%"):
    print(f"modulus of two number:{num1%num2}")
else:
    print("invalid operator ,please enter on of them as +,-,/,%,*")