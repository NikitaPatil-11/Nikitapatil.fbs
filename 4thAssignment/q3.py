#WAP to print sum of series upto n.
# WAP to print sum of series up to n

n = int(input("Enter value of n: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of series up to {n} = {total}")
