# Write a program to calculate area of rectangle

def area_of_rectangle(length, breadth):
    return length * breadth

# Taking input from user
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))

# Calling the function
area = area_of_rectangle(l, b)

print("Area of the rectangle is:", area)    

