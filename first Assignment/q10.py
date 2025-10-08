5 # Program to find the area and circumference of a circle

# Import math module for the value of pi
import math

# Input radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Display results
print(f"\nArea of the circle = {area:.2f}")
print(f"Circumference of the circle = {circumference:.2f}")

