# Program to find quotient and remainder of two numbers

# Input two numbers
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Calculate quotient and remainder
quotient = dividend // divisor
remainder = dividend % divisor

# Display results
print(f'Quotient = {quotient}')
print(f'Remainder = {remainder}')