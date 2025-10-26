# Program to convert time entered in hours, minutes, and seconds into total seconds

# Input from user
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert everything to seconds
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Output result
print(f"\nTotal time in seconds = {total_seconds} seconds")
