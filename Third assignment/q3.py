#Write a program to input angles of a triangle and check whether triangle is valid or not.

# Program to check whether a triangle is valid or not based on its angles

# Input three angles from user
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

# Check validity
if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180:
    print("\nThe triangle is valid.")
else:
    print("\nThe triangle is NOT valid.")
