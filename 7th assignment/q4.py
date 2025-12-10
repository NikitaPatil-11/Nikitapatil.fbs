n = 5  # number of rows

for i in range(1, n + 1):
    # print spaces before the numbers (for centering)
    print(" " * (n - i) * 2, end="")

    for j in range(1, i + 1):
        # print numbers only at edges and last line
        if j == 1 or j == i or i == n:
            print(j, end="  ")
        else:
            print(" ", end="  ")
    print()  # move to next line
