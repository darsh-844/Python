x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=input("Enter operation (+,-,*,/): ")

if (z=="+"):
    print ("Sum = ", x+y)

elif (z=="-"):
    print ("Difference = ", x-y)

elif (z=="*"):
    print ("Product = ", x*y)

elif (z=="/"):
    print ("Division = ", x/y)
    
else:
    print ("Invalid option")
    