# WAP to prompt user to enter userid and password
# User gets 3 chances to enter correct credentials

correct_id = "admin"
correct_password = "12345"

for attempt in range(1, 4):  # loop runs 3 times
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful! ")
        break
    else:
        print(f"Incorrect credentials! Attempts left: {3 - attempt}\n")

else:
    # This else block executes only if loop completes without break
    print("Too many failed attempts! Access Denied ")
