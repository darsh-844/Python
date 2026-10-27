#------------------------------PRIME NUMBER CHECKER------------------------------

prime=int(input("\nEnter a number to check if it is prime:"))
if prime>1:
    for i in range(2, int(prime/2)+1):
        if (prime % i) == 0:
            print(prime, "is not a prime number")
            break
    else:
        print(prime, "is a prime number")
else:
    print(prime, "is not a prime number")