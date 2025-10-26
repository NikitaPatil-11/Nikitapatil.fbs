# # Python program to swap two numbers using a third variable

# Input from user
x = int(input("Enter the first number (x): "))
y = int(input("Enter the second number (y): "))

# Display before swapping
print(f"Before swapping: x = {x}, y = {y}")

# Swapping using a third variable
z = x
x = y
y = z

# Display after swapping
print(f"After swapping: x = {x}, y = {y}")