# Program to calculate percentage based on marks in 5 subjects

# Input marks for 5 subjects
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
subject4 = int(input("Enter marks for Subject 4: "))
subject5 = int(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100  # Assuming each subject is out of 100

# Display results
print(f"\nTotal Marks: {total_marks}/500")

print(f"Percentage: {percentage:.2f}%")