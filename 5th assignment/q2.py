# Enter number of students from user. 
# For those many students accept marks of 5 subject marks from user and calculate percentage.
# Display all percentage and average percentage of students.

num_students = int(input("Enter number of students: "))

all_percentages = []  # list to store each student's percentage

for i in range(1, num_students + 1):
    print(f"\nEnter marks of 5 subjects for student {i}:")
    total = 0
    for j in range(1, 6):
        marks = float(input(f"  Subject {j} marks: "))
        total += marks

    percentage = total / 5  # since 5 subjects
    all_percentages.append(percentage)
    print(f"Percentage of student {i}: {percentage:.2f}%")

# calculate average percentage
average_percentage = sum(all_percentages) / num_students

print("\nAll students' percentages:")
for i, p in enumerate(all_percentages, start=1):
    print(f"Student {i}: {p:.2f}%")

print(f"\nAverage percentage of all students: {average_percentage:.2f}%")
 
