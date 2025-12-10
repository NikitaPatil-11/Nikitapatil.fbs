n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    # create alphabets for current row
    row = ""
    for j in range(65, 65 + (2 * i - 1)):   # 65 = ASCII of 'A'
        row += chr(j) + " "
    
    # center align the row
    print(row.center(n * 4))
