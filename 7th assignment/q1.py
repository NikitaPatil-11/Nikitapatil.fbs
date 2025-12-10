#hallow diamond shape
n = 5  # length of diamond (number of rows in top half)

# Top half of the diamond
for i in range(1, n + 1):
    print(" " * (n - i), end="")           # leading spaces
    for j in range(1, (2 * i)):            # inner pattern
        if j == 1 or j == (2 * i - 1):     # print * at borders only
            print("*", end="")
        else:
            print(" ", end="")
    print()                                # move to next line

# Bottom half of the diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")           # leading spaces
    for j in range(1, (2 * i)):            # inner pattern
        if j == 1 or j == (2 * i - 1):     # print * at borders only
            print("*", end="")
        else:
            print(" ", end="")
    print()
