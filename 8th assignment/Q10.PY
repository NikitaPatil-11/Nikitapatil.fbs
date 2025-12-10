#Write a program to check if entered year is a leap year or not.

def isLeapYear(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

year = int(input("Enter year: "))

if isLeapYear(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
