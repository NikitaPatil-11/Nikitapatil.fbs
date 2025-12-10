#Write a program to remove duplicates from the list.


li = [10, 20, 10, 30, 20, 40, 30]

new_list = []
for item in li:
    if item not in new_list:
        new_list.append(item)

print("Original List:", li)
print("List after removing duplicates:", new_list)
