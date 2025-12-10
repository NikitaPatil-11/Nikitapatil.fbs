#Write a program to find the second largest element in the list.

li = [10, 50, 30, 80, 60]

largest = second_largest = float('-inf')

for num in li:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:", second_largest)
    