n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    row = ""
    for j in range(1, (2 * i)):   # generates odd count: 1, 3, 5...
        row += str(j) + " "
    print(row.center(n * 4))
