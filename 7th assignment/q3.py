n = 5  # number of rows

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print 1st column, diagonal, or last row
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
