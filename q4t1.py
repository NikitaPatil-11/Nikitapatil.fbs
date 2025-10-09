#Calculate the cost of painting the following building walls(both interior and exterior)
#you need to accept area(one wall)and cost of both interior and exterior wall.
#note1.below diagram is of two joint rooms.
#2. it is upper view of building


# Program to calculate the cost of painting interior and exterior walls of two joined rooms

# Input section
area = float(input("Enter the area of one wall (in sq.m): "))
interior_cost = float(input("Enter the cost per sq.m for interior walls: "))
exterior_cost = float(input("Enter the cost per sq.m for exterior walls: "))

# Constants
total_walls = 7  # two rooms (8 walls) but one wall is common → 7 total

# Assuming half walls are interior and half are exterior (can adjust as needed)
interior_walls = 8
exterior_walls = 7

# Calculations
total_interior_area = interior_walls * area
total_exterior_area = exterior_walls * area

total_interior_cost = total_interior_area * interior_cost
total_exterior_cost = total_exterior_area * exterior_cost

total_painting_cost = total_interior_cost + total_exterior_cost

# Output
print("\n--- Painting Cost Summary ---")
print(f"Total interior area = {total_interior_area:.2f} sq.m")
print(f"Total exterior area = {total_exterior_area:.2f} sq.m")
print(f"Interior painting cost = ₹{total_interior_cost:.2f}")
print(f"Exterior painting cost = ₹{total_exterior_cost:.2f}")
print(f"\nTotal painting cost = ₹{total_painting_cost:.2f}")
