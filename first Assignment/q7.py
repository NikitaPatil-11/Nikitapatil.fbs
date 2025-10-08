#program to find the Roots of a quadratic equati

# Input coefficients
print("Quadratic Equation: ax² + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
D = -b +- sqrt(b**2 - 4*a*c)

# Calculate roots
root1 = (-b + D) / (2*a)
root2 = (-b - D) / (2*a)

# Output results
print(f"\nRoots of the equation are:")
print(f"Root 1 = {root1}")
print(f"Root 2 = {root2}")