#create cube od each ele in given list
# Existing list

li = [1, 2, 3, 4, 5]


# New list to store cubes
cube_list = []

for num in li:
    cube_list.append(num ** 3)

print("Original List:", li)
print("Cube List:", cube_list)



# Create an empty list
li = []

# Accept number of elements
n = int(input("How many elements you want to enter? "))

# Accept list elements from user
for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

# Create new list with cubes
cube_list = []

for x in li:
    cube_list.append(x ** 3)

# Display result
print("Original List:", li)
print("List of Cubes:", cube_list)

