  # Check if a 3-digit number is palindrome eg.121

num = int(input("Enter a 3-digit number: "))

# Ensure it's a 3-digit number
if num < 100 or num > 999:
    print("Please enter a valid 3-digit number! ")
else:
    # Reverse the number
    rev = int(str(num)[::-1])

    # Check palindrome condition
    if num == rev:
        print(f"{num} is a Palindrome! ")
    else:
        print(f"{num} is NOT a Palindrome. ")
