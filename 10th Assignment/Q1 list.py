#sum of list
def sum_of_list(li):
    total = 0
    for i in li:
        total += i
    return total

n = int(input("Enter number of elements: "))
li = [10,20,30,40,50]

for i in range(n):
    value = int(input("Enter element: "))
    li.append(value)

print("Sum =", sum_of_list(li))
