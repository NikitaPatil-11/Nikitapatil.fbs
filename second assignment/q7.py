# Program to find the sum of digits of a three-digit number

number = int(input("Enter a three-digit number: "))

# Extract digits
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

# Calculate sum
digit_sum = hundreds + tens + units

print(f"Sum of digits = {digit_sum}")