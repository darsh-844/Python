#------------------------------FACTORIAL------------------------------

c=int(input("\nEnter a number:"))
y=1
for i in range (1,c+1):
    y=y*i
print("Factorial of", c, "is", y)