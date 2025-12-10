
#Write a program find reverse of a number ,use function

def reverse_number(num):     # function with parameter
    reverse = 0
    original = num

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reverse of", original, "is:", reverse)

# Main program
n = int(input("Enter any number: "))
reverse_number(n)
