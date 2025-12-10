#Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

# Predefined list
li = [10, 20, 30, 10, 40, 50, 10, 60]

# Accept number from user
num = int(input("Enter a number to search: "))

# Count occurrences
count = li.count(num)

# Check and display result
if count > 0:
    print(num, "is present in the list", count, "time(s).")
else:
    print(num, "is NOT present in the list.")
