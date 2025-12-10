#Write a program to check if entered number is a palindrome or not. use function

def check_palindrome(num):   # function with parameter
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if original == reverse:
        print(original, "is a palindrome number")
    else:
        print(original, "is not a palindrome number")

# Main program
n = int(input("Enter any number: "))
check_palindrome(n)
