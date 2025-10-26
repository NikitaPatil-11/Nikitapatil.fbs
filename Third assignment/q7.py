#Write a program to check if user has entered correct userid and password.


# Set a predefined userid and password
correct_userid = "admin"
correct_password = "12345"

# Take input from user
userid = input("Enter User ID: ")
password = input("Enter Password: ")

# Check credentials
if userid == correct_userid and password == correct_password:
    print("\nLogin Successful! ✅")
else:
    print("\nInvalid User ID or Password ❌")

