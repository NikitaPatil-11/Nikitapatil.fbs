# WAP to print pattern:
# A
# A B
# A B C
# A B C D
# ...

n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    for j in range(65, 65 + i):     # 65 is ASCII code of 'A'
        print(chr(j), end=" ")
    print()  # move to next line
