# Write a program to find sum of following series using functions : 1!+ 2! + 3! + 4!+..... + n! 
def sum_factorial_series(n):     # function with parameter
    total = 0
    
    # calculate factorial and add
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact = fact * j
        total += fact

    print("Sum of the series 1! + 2! + ... +", n, "!= ", total)

# Main program
num = int(input("Enter the value of n: "))
sum_factorial_series(num)

