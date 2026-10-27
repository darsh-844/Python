#------------------------------FIBONACCI SERIES------------------------------

t=int(input("\nEnter a number for series:"))
z=1
d=0
print("Fibonacci series up to", t, "terms:")
for i in range(0,t):
    d=z+d
    z=d-z
    print(z)
