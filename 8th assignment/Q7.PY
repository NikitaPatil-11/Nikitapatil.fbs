def sum_of_digits(num):     # function with parameter
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    print("Sum of digits =", total)

# Main program
n = int(input("Enter any number: "))
sum_of_digits(n)
