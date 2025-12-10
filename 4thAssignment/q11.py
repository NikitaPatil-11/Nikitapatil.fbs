#WAP to check if given number Strong Number.
import math

# Input from user
num = int(input("Enter a number: "))
original = num
sum_of_factorials = 0

# Calculate sum of factorials of digits
while num > 0:
    digit = num % 10
    sum_of_factorials += math.factorial(digit)
    num = num // 10

# Check condition
if sum_of_factorials == original:
    print(f"{original} is a Strong Number.")
else:
    print(f"{original} is NOT a Strong Number.")