#Write a program to create a duplicate of an existing list. It should not point to same list.

# Original list
li = [10, 20, 30, 40, 50]

# Create duplicate list (true copy)
dup_list = li.copy()     # or dup_list = li[:]

print("Original List:", li)
print("Duplicate List:", dup_list)

# Check if both lists point to different memory locations
print("Same memory? ->", li is dup_list)
