#Write a program of having n number of elements in the list and find out even 
# and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.

# Create empty lists
li = []
even_list = []
odd_list = []

# Accept number of elements
n = int(input("How many elements you want to enter? "))

# Accept list elements
for i in range(n):
    num = int(input("Enter element: "))
    li.append(num)

# Separate even and odd numbers
for x in li:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

# Display results
print("Original List:", li)
print("Even List:", even_list)
print("Odd List:", odd_list)
