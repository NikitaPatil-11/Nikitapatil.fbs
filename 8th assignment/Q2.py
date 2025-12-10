#Write a program to calculate area of circle
def area_of_circle(radius):   # function with parameter
    area = 3.14 * radius * radius
    print("Area of the circle is:", area)

# Main program
r = float(input("Enter radius of the circle: "))
area_of_circle(r)     # passing the value to function
