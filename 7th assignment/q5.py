n = 5  # number of rows

for i in range(1, n + 1):
    # print leading spaces
    print(" " * (n - i), end= " ")

    # print increasing numbers
    num = i
    for j in range(1, i + 1):
        print(num, end= " ")
        num += 1

    # print decreasing numbers
    num -= 2
    for j in range(1, i):
        print(num, end= " ")
        num -= 1

    print()  # move to next line
