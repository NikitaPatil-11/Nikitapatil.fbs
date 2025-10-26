# Program to convert distance given in feet and inches into meters and centimeters

# Input from user
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter remaining inches: "))

# Convert to total inches
total_inches = (feet * 12) + inches

# Convert inches to centimeters
total_cm = total_inches * 2.54

# Convert centimeters to meters and centimeters
meters = int(total_cm // 100)
centimeters = total_cm % 100

# Output
print(f"\nEquivalent distance:")
print(f"{meters} meter(s) and {centimeters:.2f} centimeter(s)")
