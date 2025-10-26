#Write a program to input any alphabet and check whether it is vowel or consonant.
# Program to check whether a given alphabet is a vowel or consonant

# Input from user
x = input("Enter any alphabet: ")

# Convert to lowercase to handle both upper and lower case inputs
x = x.lower()

# Check if it's a vowel
if x in ('a', 'e', 'i', 'o', 'u'):
    print(f"{x} is a vowel.")
elif x.isalpha():  # checks if it's a letter
    print(f"{x} is a consonant.")
else:
    print("Invalid input! Please enter an alphabet.")
