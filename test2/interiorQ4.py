

# Program to calculate the total cost of painting the interior walls of a building

# Input dimensions and cost rate
length = float(input("Enter the length of a wall (in meters): "))
height = float(input("Enter the height of a wall (in meters): "))
rate = float(input("Enter the cost of painting per square meter: "))

# Calculate total area and cost
area = 4 * (length * height)
total_cost = area * rate

# Display result
print("\n----- Painting Cost Summary -----")
print(f"Total area of 4 walls = {area:.2f} sq. meters")
print(f"Cost per square meter = ₹{rate:.2f}")
print(f"Total Painting Cost = ₹{total_cost:.2f}")
