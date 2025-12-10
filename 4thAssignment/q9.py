# WAP to print all numbers in a range divisible by a given number

# take inputs from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
divisor = int(input("Enter the number to divide by: "))

print(f"Numbers between {start} and {end} divisible by {divisor} are:")

for i in range(start, end + 1):
    if i % divisor == 0:
        print(i)
