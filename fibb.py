x=int(input("Enter the number of terms: "))
y=0
z=1

for i in range (0,x):
    y=z+y
    z=y-z
    print(z)
    
a=int(input("Enter the term for which you want to find the fibonacci number: "))
b=0
c=1
for i in range (0,a):
    b=c+b
    c=b-c
print("Fibonacci number at ",a," term is ", c)
    