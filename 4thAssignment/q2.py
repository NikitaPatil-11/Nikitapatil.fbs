## Program to print all odd numbers until n

n = int(input("Enter the value of n: "))

print(f"odd numbers from 1 to {n}:")

for i in range(1, n + 1, 2):   
    print(i)
