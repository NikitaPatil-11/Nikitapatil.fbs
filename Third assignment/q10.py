#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)


m = int(input("Enter age of male: "))
f = int(input("Enter age of female: "))

if m >= 21 and f >= 18:
    print(" The couple is eligible to marry.")
else:
    print(" The couple is not eligible to marry.")
