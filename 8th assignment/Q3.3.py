#1^1 + 2^2 + 3^3+ ...... n^n 
def sum_power_series(n):     # function with parameter
    total = 0
    for i in range(1, n + 1):
        total += i ** i      # i raised to the power i
    print("Sum of power series is:", total)   # no return value

# Main program
num = int(input("Enter the value of n: "))
sum_power_series(num)        # passing parameter


