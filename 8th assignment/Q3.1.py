#Write a program to find sum of following series using functions :  1+ 2 + 3 + 4+..... + n

def sum_series(n):      # function with parameter
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum of the series is:", total)   # no return value

# Main program
num = int(input("Enter the value of n: "))
sum_series(num)         # passing the value
