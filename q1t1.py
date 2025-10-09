#wap to find the area and perimeter of give fig (accept length, breadth, radius)
# It is a square+half circle

# Program: Combined area and perimeter of a 3-sided square and a half-circle

# --- Square with 3 sides 
side = float(input("Enter the side of the square: "))

# Square calculations
square_area = side ** 2                # same area formula
square_perimeter = 3 * side            # only 3 sides instead of 4

# --- Half Circle ---
radius = float(input("\nEnter the radius of the circle: "))

# Area of half circle = (1/2) * π * r²
# Perimeter = πr + 2r  (half circumference + diameter)
half_circle_area = 0.5 * 3.142 * radius ** 2
half_circle_perimeter = 3.142 * radius + 2 * radius

# --- Combined Results ---
total_area = square_area + half_circle_area
total_perimeter = square_perimeter + half_circle_perimeter

# --- Display results ---
print("\n--- Results ---")
print(f"Square area = {square_area:.2f}")
print(f"Half circle area = {half_circle_area:.2f}")
print(f"Total area = {total_area:.2f}")

print(f"\nSquare perimeter (3 sides) = {square_perimeter:.2f}")
print(f"Half circle perimeter = {half_circle_perimeter:.2f}")
print(f"Total perimeter = {total_perimeter:.2f}")


