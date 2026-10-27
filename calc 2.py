#------------------------------CALCULATOR------------------------------

x=float(input("Enter a number:"))
y=float(input("Enter another number:"))
op=input("Enter an operation (+, -, *, /): ")
if op=="+":
    result=x+y
elif op=="-":
    result=x-y
elif op=="*":
    result=x*y
elif op=="/":
    if y!=0:
        result=x/y
    else:
        result="Error"
else:
    result="INVALID OPERATION"
print("Result =", result)