a=int(input("Enter a number: "))
sum=0
temp=a
while temp>0:
    digit=temp%10
    x=len(str(a))
    sum+=digit**x
    temp//=10
if a==sum:
    print(a,"is an Armstrong number")
else:
    print(a,"is not an Armstrong number")   
