#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# Program to check whether the triangle is equilateral, isosceles or scalene

# Input sides of triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# First, check if it's a valid triangle (triangle inequality rule)
if (a + b > c) and (a + c > b) and (b + c > a):
    # Then check type of triangle
    if a == b == c:
        print("\nThe triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("\nThe triangle is Isosceles.")
    else:
        print("\nThe triangle is Scalene.")
else:
    print("\nThe given sides do NOT form a valid triangle.")
