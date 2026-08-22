x=int(input("Enter a number: "))
sum=0
y=x

while x>0:
    sum+=x%10
    x=x//10

print ("Sum of the digits of", y, "is = ", sum)
    