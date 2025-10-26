# Python program to swap two numbers without using a third variable

# Input from user
x = int(input("Enter the first number (x): "))
y = int(input("Enter the second number (y): "))

# Display before swapping
print(f"Before swapping: x = {x}, y = {y}")

# Swapping without using a third variable
x = x + y
y = x - y
x = x - y

# Display after swapping
print(f"After swapping: x = {x}, y = {y}")