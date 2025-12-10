# WAP to find sum of series: 1! + 2! + 3! + ... + n!

n = int(input("Enter the value of n: "))

sum_fact = 0

fact = 1
for i in range(1, n + 1):
    fact *= i           # calculate factorial step-by-step
    sum_fact += fact    # add factorial to sum

print("Sum of the series 1! + 2! + 3! + ... +", n, "! =", sum_fact)
