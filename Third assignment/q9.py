# Program to input marks of 5 subjects and display grade

# Input marks
s1 = float(input("Enter marks of Subject 1: "))
s2 = float(input("Enter marks of Subject 2: "))
s3 = float(input("Enter marks of Subject 3: "))
s4 = float(input("Enter marks of Subject 4: "))
s5 = float(input("Enter marks of Subject 5: "))

# Calculate total and percentage
total = s1 + s2 + s3 + s4 + s5
percentage = (total / 500) * 100   # assuming each subject is out of 100

# Display percentage
print(f"\nTotal Marks = {total}/500")
print(f"Percentage = {percentage:.2f}%")

# Determine grade/class
if percentage >= 75:
    print("Grade: Distinction ")
elif percentage >= 60:
    print("Grade: First Class ")
elif percentage >= 50:
    print("Grade: Second Class ")
elif percentage >= 35:
    print("Grade: Pass ")
else:
    print("Grade: Fail ")
