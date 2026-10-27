#------------------------------FIBONACCI NUMBER------------------------------

a=int(input("\nEnter the term for which you want to find the fibonacci number: "))
b=0
c=1
for i in range (0,a):
    b=c+b
    c=b-c
print("Fibonacci number at ",a,"th term is ", c)