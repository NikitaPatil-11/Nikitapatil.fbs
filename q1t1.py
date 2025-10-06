#programme to find area and parameter of following dia.
import math

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def half_circle_area(radius):
    return (math.pi * radius ** 2) / 2

def half_circle_perimeter(radius):
    # Perimeter includes the curved part and the diameter
    return math.pi * radius + 2 * radius

# Input from user
print("Enter dimensions for the rectangle:")
length = float(input("Length: "))
width = float(input("Width: "))

print("\nEnter radius for the half circle:")
radius = float(input("Radius: "))

# Rectangle calculations
rect_area = rectangle_area(length, width)
rect_perimeter = rectangle_perimeter(length, width)

# Half circle calculations
half_area = half_circle_area(radius)
half_perimeter = half_circle_perimeter(radius)

# Output results
print("\n--- Results ---")
print(f"Rectangle Area: {rect_area:.2f}")
print(f"Rectangle Perimeter: {rect_perimeter:.2f}")
print(f"Half Circle Area: {half_area:.2f}")
print(f"Half Circle Perimeter: {half_perimeter:.2f}")




