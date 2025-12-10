#Write a program to remove all occurrences of a given element in the list.

# Create list
li = []

# Accept number of elements
n = int(input("How many elements you want to enter? "))

# Accept list elements
for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

# Accept element to remove
item = int(input("Enter element to remove: "))

# Remove all occurrences
while item in li:
    li.remove(item)

# Display result
print("Updated List:", li)
