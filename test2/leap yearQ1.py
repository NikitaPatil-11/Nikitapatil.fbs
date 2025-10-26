#write a program to accpet year from user and check if it is a leap year or not
#condition leap year366


y = int(input("Enter a Year: "))

# Leap year conditions:
#  Divisible by 400 → Leap year
# Divisible by 4 but not by 100 → Leap year
# Otherwise → Not a leap year

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print("It is a Leap Year ")
else:
    print("It is NOT a Leap Year ")
