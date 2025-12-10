n = 5  # number of rows

for i in range( 1, n + 1):
    # print spaces for center alignment
    print(" " * (n - i), end=" ")

    # print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # move to next line
