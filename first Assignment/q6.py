#write a programme to input two angles from user and third angle of the triangle

# Input two angles from user
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))

# Calculate third angle
angle3 = 180 - (angle1 + angle2)

# Display the result
print(f'\nThe third angle of the triangle is: {angle3} degrees')
