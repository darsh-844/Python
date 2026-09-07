
# while temp>0:
#     digit=temp%10
#     x=len(str(a))
#     sum+=digit**x
#     temp//=10

def armstrong(a):
    sum=0
    temp=a
    x=len(str(a))
    while temp>0:
        digit=temp%10
        sum+=digit**x
        temp//=10
    return sum

a=int(input("Enter a number: "))
sum=armstrong(a)
if a==sum:
     print(a,"is an Armstrong number")
else:
     print(a,"is not an Armstrong number")   

