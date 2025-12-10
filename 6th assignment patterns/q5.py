#write a program

rows = int(input("Enter number of rows: "))

for i in range(rows):
    # Print spaces for center alignment
    print(' ' * (rows - i), end='')


    for j in range(i + 1):
        print('*', end=' ')
        num = (i - j) // (j + 1)
    print()  # move to next line
