a=int(input("enter a number:"))
op=input("enter operator(+,-,*,/,%):")
b=int(input("enter a second number"))
if op=='+':
    print("result:",a+b)
elif op=='-':
    print("result:",a-b)
elif op=='*':
    print("result:",a*b)
elif op=='/':
    print("result:",a/b)
elif op=='%':
    print("result:",a%b)
else:
    print("invalid operator")
    