#sum of all odd numbers between 1 to n

def sum_of_odds(n):      # function with parameter
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:   # check odd number
            total += i
    print("Sum of all odd numbers is:", total)   # without return value

# Main program
num = int(input("Enter the value of n: "))
sum_of_odds(num)
