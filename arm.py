#------------------------------ARMSTRONG NUMBER CHECKER------------------------------

def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == num

armstrong=int(input("\nEnter a number to check if it is an Armstrong number: "))
if is_armstrong(armstrong):
    print(armstrong, "is an Armstrong number")
else:
    print(armstrong, "is not an Armstrong number")
    